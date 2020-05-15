This is a python interface to the [are.na](https://www.are.na/) [API](https://dev.are.na/documentation).

## Installation

    pip install arena

## Example

Bulk adding urls to a channel:

```
from arena import Arena
arena = Arena(my_access_token)

chan = arena.channels.channel('<channel-slug>')
for url in urls:
    chan.add_block(source=url)
```

## Documentation

### Basic usage

You first need an access token, which you can obtain via the authentication flow (below) or by creating [a new application](https://dev.are.na/) and grabbing the access token shown after creation.

```
from arena import Arena
arena = Arena(my_access_token)
arena.channels.channel('faq')
```

### Pagination

Endpoints which support pagination accept the keyword arguments `page` (1-indexed) and `per_page`. They return a tuple consisting of the results for that page and pagination info.

For example:

    chans, page = arena.channels.list(page=1, per_page=10)

### Data

Resources (Block, Channel, User) have a nested `.data` attribute that contains the raw API fields return from the are.na API. For example:
```python
channels, page = user.channels()
for chanl in channels:
    if chanl.data['status'] not in ['private', 'closed']:
        ...
```

### Channels

#### Listing channels

    chans, page = arena.channels.list(page=1, per_page=10)

#### Creating a new channel

    arena.channels.create(title='My Channel', status='public')

`status` can be one of `['public', 'private', 'closed']`.

#### Getting an existing channel

By slug:

    arena.channels.channel('yuppie-dystopia')

#### Searching channels

    arena.channels.search('climate')

#### Getting the contents of a channel

    chan = arena.channels.channel('yuppie-dystopia')
    items, page = chan.contents()

#### Getting the connections of a channel

    # Low-fidelity
    chans, page = chan.connections()

    # High-fidelity
    chans, page = chan.channels()

### Getting the collaborators of a channel

    users, page = chan.collaborators()

#### Adding/removing blocks from the channel

(This is also how you create blocks in general.)

    # A block is added as a url
    block = chan.add_block(source='https://github.com/frnsys/arena')

    # Or as content
    block = chan.add_block(content='Hello are.na')

    # Removing a block
    chan.remove_block(block_id)

#### Deleting a channel

    chan.delete()

### Blocks

#### Getting an existing block

By id:

    arena.blocks.block('896296')

#### Searching blocks

    arena.blocks.search('climate')

#### Creating a new block

Blocks are created via the channel API (see above).

#### Updating a block

    block = arena.blocks.block('896296')
    block.update(title='Burrito Galaxy', description='A cool game')

Note that text block also support the `content` argument, which supports markdown.

#### Getting channels for a block

    block = arena.blocks.block('896296')
    chans, page = block.channels()

### Users

#### Getting an existing user

By slug:

    arena.users.user('francis-tseng')

#### Searching users

    arena.users.search('climate')

#### Getting a user's channels

    user = arena.users.user('francis-tseng')
    chans, page = user.channels()

#### Getting a user's following/followers

    user = arena.users.user('francis-tseng')
    following, page = user.following()
    followers, page = user.followers()

Note that `following` can include users _and_ channels.

### Feed

To get the authenticated user's feed:

    items, page = arena.feed(offset=0)

### Authentication

```
from arena import Auth

auth_flow = Auth(
    client_id=YOUR_CLIENT_ID,
    client_secret=YOUR_CLIENT_SECRET,
    callback_url=YOUR_CALLBACK_URL,
)

# Direct your user to this request url,
# which redirects them to YOUR_CALLBACK_URL/?code=CODE
request_url = auth_flow.request_url()

# Using the provided CODE:
resp = auth_flow.request_access_token(CODE)

access_token = resp['access_token']
```

## Testing

Export your Are.na token as an environment variable called `ARENA`, then run `nosetests`, e.g.:

```
export ARENA=my-token
nosetests tests
```
