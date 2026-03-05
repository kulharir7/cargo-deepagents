# React Patterns

## Component Structure

function ComponentName({ prop1, prop2 }) {
    // State hooks
    const [state, setState] = useState(initialValue);
    
    // Effect hooks
    useEffect(() => {
        // Side effect
        return () => {
            // Cleanup
        };
    }, [dependencies]);
    
    // Event handlers
    const handleClick = () => {
        setState(newValue);
    };
    
    // Render
    return (
        <div className="container">
            <h1>{prop1}</h1>
            <button onClick={handleClick}>{prop2}</button>
        </div>
    );
}

## Custom Hooks

function useFetch(url) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        fetch(url)
            .then(res => res.json())
            .then(setData)
            .catch(setError)
            .finally(() => setLoading(false));
    }, [url]);
    
    return { data, loading, error };
}

## Performance

// Memoized component
const MemoComponent = memo(ExpensiveComponent);

// Memoized value
const sorted = useMemo(() => 
    items.sort((a, b) => a.name.localeCompare(b.name)),
    [items]
);

// Memoized callback
const handleClick = useCallback(() => {
    doSomething(deps);
}, [deps]);
