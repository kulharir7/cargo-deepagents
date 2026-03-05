"""Cloud MCP Server - AWS/GCP/Azure"""
import asyncio
import subprocess
import json
from typing import List, Dict, Any
from mcp.server import Server
from mcp.types import Tool, TextContent

class CloudMCPServer:
    def __init__(self, name="cloud-mcp"):
        self.server = Server(name)
        self._setup_handlers()
    
    def _run(self, cmd):
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        return result.returncode, result.stdout, result.stderr
    
    def _setup_handlers(self):
        @self.server.list_tools()
        async def list_tools():
            return [
                # AWS
                Tool(name="aws_ec2_list", description="List EC2", inputSchema={"type": "object", "properties": {"region": {"type": "string"}}}),
                Tool(name="aws_ec2_start", description="Start EC2", inputSchema={"type": "object", "properties": {"instance_id": {"type": "string"}}, "required": ["instance_id"]}),
                Tool(name="aws_ec2_stop", description="Stop EC2", inputSchema={"type": "object", "properties": {"instance_id": {"type": "string"}}, "required": ["instance_id"]}),
                Tool(name="aws_s3_list", description="List S3", inputSchema={"type": "object", "properties": {}}),
                Tool(name="aws_s3_upload", description="Upload S3", inputSchema={"type": "object", "properties": {"file": {"type": "string"}, "bucket": {"type": "string"}}, "required": ["file", "bucket"]}),
                Tool(name="aws_s3_download", description="Download S3", inputSchema={"type": "object", "properties": {"bucket": {"type": "string"}, "key": {"type": "string"}}, "required": ["bucket", "key"]}),
                Tool(name="aws_lambda_list", description="List Lambda", inputSchema={"type": "object", "properties": {}}),
                Tool(name="aws_lambda_invoke", description="Invoke Lambda", inputSchema={"type": "object", "properties": {"function": {"type": "string"}}, "required": ["function"]}),
                # GCP
                Tool(name="gcp_compute_list", description="List GCP VMs", inputSchema={"type": "object", "properties": {}}),
                Tool(name="gcp_storage_ls", description="List GCP Storage", inputSchema={"type": "object", "properties": {}}),
                # Azure
                Tool(name="azure_vm_list", description="List Azure VMs", inputSchema={"type": "object", "properties": {}}),
                Tool(name="azure_vm_start", description="Start Azure VM", inputSchema={"type": "object", "properties": {"name": {"type": "string"}, "rg": {"type": "string"}}, "required": ["name", "rg"]}),
                Tool(name="azure_vm_stop", description="Stop Azure VM", inputSchema={"type": "object", "properties": {"name": {"type": "string"}, "rg": {"type": "string"}}, "required": ["name", "rg"]}),
                # Status
                Tool(name="cloud_status", description="Cloud status", inputSchema={"type": "object", "properties": {}})
            ]
        
        @self.server.call_tool()
        async def call_tool(name, arguments):
            region = arguments.get("region", "us-east-1")
            if name == "aws_ec2_list":
                cmd = f"aws ec2 describe-instances --region {region} --output json"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "aws_ec2_start":
                cmd = f"aws ec2 start-instances --instance-ids {arguments['instance_id']} --region {region}"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=f"Started: {arguments['instance_id']}" if code == 0 else err)]
            elif name == "aws_ec2_stop":
                cmd = f"aws ec2 stop-instances --instance-ids {arguments['instance_id']} --region {region}"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=f"Stopped: {arguments['instance_id']}" if code == 0 else err)]
            elif name == "aws_s3_list":
                cmd = "aws s3 ls"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "aws_s3_upload":
                cmd = f"aws s3 cp {arguments['file']} s3://{arguments['bucket']}/"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text="Uploaded" if code == 0 else err)]
            elif name == "aws_s3_download":
                cmd = f"aws s3 cp s3://{arguments['bucket']}/{arguments['key']} ."
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text="Downloaded" if code == 0 else err)]
            elif name == "aws_lambda_list":
                cmd = f"aws lambda list-functions --region {region} --output json"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "aws_lambda_invoke":
                cmd = f"aws lambda invoke --function-name {arguments['function']} /dev/stdout"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "gcp_compute_list":
                cmd = "gcloud compute instances list"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "gcp_storage_ls":
                cmd = "gsutil ls"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "azure_vm_list":
                cmd = "az vm list --output json"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=out if code == 0 else err)]
            elif name == "azure_vm_start":
                cmd = f"az vm start --name {arguments['name']} --resource-group {arguments['rg']}"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=f"Started: {arguments['name']}" if code == 0 else err)]
            elif name == "azure_vm_stop":
                cmd = f"az vm stop --name {arguments['name']} --resource-group {arguments['rg']}"
                code, out, err = self._run(cmd)
                return [TextContent(type="text", text=f"Stopped: {arguments['name']}" if code == 0 else err)]
            elif name == "cloud_status":
                results = {}
                for cloud, cmd in [("aws", "aws --version"), ("gcp", "gcloud --version"), ("azure", "az --version")]:
                    code, _, _ = self._run(cmd)
                    results[cloud] = "configured" if code == 0 else "not configured"
                return [TextContent(type="text", text=json.dumps(results, indent=2))]
            return [TextContent(type="text", text=f"Unknown: {name}")]
    
    async def run(self):
        from mcp.server.stdio import stdio_server
        async with stdio_server() as (rs, ws):
            await self.server.run(rs, ws, {})

async def main():
    await CloudMCPServer().run()

if __name__ == "__main__":
    asyncio.run(main())
