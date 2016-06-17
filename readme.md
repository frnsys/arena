this is a python interface to the [are.na](https://www.are.na/) API.

it's still in a preliminary untested state!

## installation

    pip install arena


## usage

    from arena import Arena
    api = Arena(my_access_token)
    api.channels.channel('faq')

## todo

- tests
- authentication flow
- wrap responses in objects? e.g. Channel, User, etc