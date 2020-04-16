import time

from urllib.parse import quote
from urllib import request
import gzip

import hmac
from hashlib import sha256
from base64 import b64encode

class Amazon:    

    def __init__(self, awsAccessKeyId=None, awsSecretAccessKey=None,
        associateTag=None):
        
        self.awsAccessKeyId = awsAccessKeyId
        self.awsSecretAccessKey = awsSecretAccessKey
        self.associateTag = associateTag        
        self.operation = None        


    def __call__(self, **kwargs): 

        api_url = self._get_api_url(**kwargs).replace('webservices.amazon.com','com.commercedna.com')                
        response = self._call_api(api_url)        
        response_text = response.read().decode('UTF-8')

        return response_text
        

    def __getattr__(self, operation):     

        self.operation = operation

        return self


    def _call_api(self, api_url):
        api_request = request.Request(api_url, headers={"Accept-Encoding": "gzip"})
            
        try:                
            return request.urlopen(api_request)
        except:
            raise


    def _get_api_responsegroup(self, operation):

        if operation == 'ItemSearch' or  operation == 'SimilarityLookup':
            return ('Accessories,AlternateVersions,BrowseNodes,EditorialReview,' + 
            'Images,ItemAttributes,ItemIds,Large,Medium,OfferFull,OfferListings,Offers,OfferSummary,' + 
            'PromotionSummary,Reviews,SalesRank,SearchBins,Similarities,Small,Tracks,' + 
            'Variations,VariationMatrix,VariationOffers,VariationSummary')
        elif operation == 'ItemLookup':
            return ('ItemIds,Small,Medium,Large,Offers,OfferFull,OfferSummary,OfferListings,' + 
            'PromotionSummary,Variations,VariationImages,VariationSummary,' + 
            'VariationMatrix,VariationOffers,ItemAttributes,Tracks' + 
            'Accessories,EditorialReview,SalesRank,BrowseNodes,Images,Similarities,Reviews',
            'SearchInside,PromotionalTag,AlternateVersions,Collections,ShippingCharges')
        elif operation == 'BrowseNodeLookup':
            return 'BrowseNodeInfo,MostGifted,NewReleases,MostWishedFor,TopSellers'

        raise Exception(f'The {operation} is not supported.')


    def _get_api_url(self, **kwargs):
        
        query = {
            'Service': "AWSECommerceService",
            'AWSAccessKeyId': self.awsAccessKeyId,
            'Operation': self.operation,            
            'Timestamp': time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }        

        if self.associateTag:
            query['AssociateTag'] = self.associateTag

        api_responsegroup = self._get_api_responsegroup(self.operation)

        if api_responsegroup:
            query['ResponseGroup'] = api_responsegroup
        
        query.update(kwargs)        
        
        query_string = self._build_query(query)

        data = f"GET\nwebservices.amazon.com\n/onca/xml/\n{query_string}"

        if type(self.awsSecretAccessKey) is str:
            self.awsSecretAccessKey = self.awsSecretAccessKey.encode('utf-8')

        if type(data) is str:
            data = data.encode('utf-8')

        digest = hmac.new(self.awsSecretAccessKey, data, sha256).digest()

        signature = quote(b64encode(digest))     

        return f"https://webservices.amazon.com/onca/xml/?{query_string}&Signature={signature}"


    def _build_query(self, query):
        """Build query string from the dictionary"""    
        return "&".join("%s=%s" % (
            key, quote(
                str(query[key]).encode('utf-8'), safe='~'))
                for key in sorted(query))