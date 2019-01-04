this is a python interface to the [are.na](https://www.are.na/) [API](https://dev.are.na/documentation).

it's still in a preliminary untested state!

## Installation

    pip install arena


## Usage

    from arena import Arena
    arena = Arena(my_access_token)
    arena.channels.channel('faq')

More complete documentation coming soon

## API parity progress

- [ ] Authentication
- [ ] Blocks
- [ ] Channels
- [x] Search
- [x] Users

## Example

Bulk adding urls to a channel:

```
from arena import Arena
arena = Arena(my_access_token)

chan = arena.channels.channel('<channel-slug>')
for url in urls:
    chan.add_block(source=url)
```

## Testing

Export your Are.na token as an environment variable called `ARENA`, then run `nosetests`, e.g.:

```
export ARENA=my-token
nosetests tests
```
