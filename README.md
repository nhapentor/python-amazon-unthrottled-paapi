Amazon Unthrottled Access to Amazon Product Advertising API for Python
=======================================================
A plain simple Python client for [Amazon Product Advertising API](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/Welcome.html). This client is implemented following this [Node.js API client](https://www.npmjs.com/package/amazon-unthrottled-api) to gives you unthrottled access to Amazon product data using a [shared cache](https://www.commercedna.com/). Therefore it might not comply with the Amazon's specifications.



[![License](https://img.shields.io/badge/License-MIT-%23e83633)](https://github.com/sergioteula/python-amazon-paapi/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-%231182C2)](https://www.python.org/)


Features
--------
* Access to Amazon product data from a caching service provided by [CommerceDNA](https://www.commercedna.com/), so you no longer run into the RequestThrottled error.


Dependencies
--------------
* An Amazon Product Advertising account
* AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and AWS_ASSOCIATE_TAG


Installation
-------------
     pip install python-amazon-unthrottled-paapi


Usage
-----
Import library

```python
from amazon.api import Amazon
```


Create client

```python
amazon_client = Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)
```


ItemSearch

The ItemSearch operation searches for items on Amazon. The Product Advertising API returns up to ten items per search results page.

```python
response_text = amazon_client.ItemSearch(keywords: 'Quentin Tarantino', searchIndex: 'DVD')
```

ItemLookup

Given an Item identifier, the ItemLookup operation returns some or all of the item attributes, depending on the response group specified in the request.

```python
response_text = amazon_client.ItemLookup(IdType='UPC', ItemId='884392579524')
```

BrowseNodeLookup

Given a browse node ID, BrowseNodeLookup returns the specified browse node’s name, children, and ancestors. The names and browse node IDs of the children and ancestor browse nodes are also returned. BrowseNodeLookup enables you to traverse the browse node hierarchy to find a browse node.

```python
response_text = amazon_client.BrowseNodeLookup(BrowseNodeId='549726')
```


License
-------
Copyright &copy; 2020 [apptiviz](https://www.apptiviz.com)

See [MIT License](LICENSE) for details.