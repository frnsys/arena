this is a python interface to the [are.na](https://www.are.na/) [API](https://dev.are.na/documentation).

it's still in a preliminary untested state!

## installation

    pip install arena


## usage

    from arena import Arena
    arena = Arena(my_access_token)
    arena.channels.channel('faq')

## todo

- tests
- documentation
- authentication flow

## api parity progress

- [ ] Authentication
- [ ] Blocks
- [ ] Channels
- [x] Search
- [x] Users

## example

Bulk adding urls to a channel:

```
import arena
from arena.channels import Channel
arena.access_token = '<YOUR ACCESS TOKEN>'

chan = Channel('<channel-slug>')
for url in urls:
    chan.add_block(source=url)
```
