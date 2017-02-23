this is a python interface to the [are.na](https://www.are.na/) [API](https://dev.are.na/documentation).

it's still in a preliminary untested state!

## installation

    pip install arena


## usage

    from arena import Arena
    api = Arena(my_access_token)
    api.channels.channel('faq')

## todo

- tests
- documentation
- authentication flow
- wrap responses in objects? e.g. Channel, User, etc