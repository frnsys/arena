this is a python interface to the [are.na](https://www.are.na/) [API](https://dev.are.na/documentation).

it's still in a preliminary untested state!

## installation

    pip install arena


## usage

    import arena
    arena.access_token = my_access_token
    arena.channels.channel('faq')

## todo

- tests
- documentation
- authentication flow
- wrap responses in objects? e.g. Channel, User, etc

## api parity progress

- [ ] Authentication
- [ ] Blocks
- [ ] Channels
- [x] Search
- [x] Users
