# Tailwind Cheatsheet

## Layout

container       # Max-width container
flex            # display: flex
grid            # display: grid
hidden          # display: none

## Spacing

p-4             # padding: 1rem
px-4            # padding-left/right: 1rem
py-4            # padding-top/bottom: 1rem
m-4             # margin: 1rem
mx-auto         # margin-left/right: auto (center)

## Sizing

w-full          # width: 100%
h-screen        # height: 100vh
max-w-lg        # max-width: 32rem

## Flexbox

justify-center  # justify-content: center
items-center    # align-items: center
gap-4           # gap: 1rem

## Typography

text-xl         # font-size: 1.25rem
font-bold       # font-weight: 700
text-center     # text-align: center
text-gray-600   # color: gray-600

## Background

bg-white        # background-color: white
bg-blue-500     # background-color: blue-500

## Border

border          # border: 1px solid
rounded         # border-radius: 0.25rem
rounded-lg      # border-radius: 0.5rem

## Responsive

sm:text-lg      # @media (min-width: 640px)
md:grid-cols-2  # @media (min-width: 768px)
lg:grid-cols-3  # @media (min-width: 1024px)
xl:w-1/2        # @media (min-width: 1280px)

## Hover/States

hover:bg-blue-700
focus:ring
active:scale-95
disabled:opacity-50
