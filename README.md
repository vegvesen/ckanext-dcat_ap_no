# ckanext-dcat_ap_no

This is a collection of stuff needed to make CKAN conform to DCAT-AP-NO, the Norwegian adaption of the DCAT-AP standard. (It's compatible with DCAT-AP, but has a few additional fields.) It can be found here: https://doc.difi.no/dcat-ap-no/

The code currently validates without errors (but with warnings) against Difi's DCAT harvester at http://demo.difi.no/dcat-admin-webapp/admin (contact opnedata@difi.no for username/password). 
NB! There is no validation in this plugin of most of the fields. For instance, it's possible to enter text in fields which are expected by the standard to be URIs. If you do, the catalog will fail validation.

dcat_ap_no_schema.json contains fields to be shown on each dataset page, with suggested values and help text
profiles.py determines how to map the fields to the DCAT-AP-NO standard

#### Note!

Currently, the catalog is shown just fine as catalog.jsonld and catalog.xml, but catalog.ttl and catalog.n3 give error message (server error).
TODO: Fix this!

## Requirements

Install the plugins `ckanext-dcat` and `ckanext-scheming` and configure them accordingly.

#### Note!

Until `ckanext-dcat` has merged [PR#66](https://github.com/ckan/ckanext-dcat/pull/66) you have to install from the fork using
    
    (pyenv) $ pip install -e git+https://github.com/vegvesen/ckanext-dcat.git@feature/dcat-ap11#egg=ckanext-dcat

TODO: This should be OK now, test and remove note if so.
    
## Installation

1.  Install the package

        (pyenv) $ pip install -e git+https://github.com/vegvesen/ckanext-dcat_ap_no.git#egg=ckanext-dcat_ap_no

2.  Set the dcat profile in your configuration file:

        ckanext.dcat.rdf.profiles = norwegian_dcat_ap

3.  Enable the dataset schema in your configuration file:

        scheming.dataset_schemas = ckanext.dcat_ap_no:dcat_ap_no_schema.json
        
4.  Add publisher info to your configuration file (required by the rdf profile):
  
        ckan.publisher.name = Your name
        ckan.publisher.email = someone@domain.no
        ckan.publisher.webpage = http://domain.no
        
5. Add catalog info to your configuration file

        ckan.catalog.license_url = http://domain.no/license
        ckan.catalog.theme_url = http://domain.no/theme
        ckan.catalog.issued = 2016-09-16T10:27:55.249666
        
        
## Additional information + TODOs

### Schema specified in dcat_ap_no_schema.json

The field dcat_ap_no_comment is used to list the field's corresponding URI in the standard. It will not be displayed, and is just used as a comment for information.

For most of the fields, we can't support cardinality greater than 1.

#### Datasets

Comments regarding some fields:

* dcat:contactPoint: Only email is given as contact info, additional contact info should be added
* dcat:distribution: Resource is used for this (this is identical to how it's done in the plugin `ckanext-dcat`)
* adms:sample: Not mapped, should use Resource with a new field indicating that this is an example
* dct:spatial: Only spatial_text included in dcat_ap_no_schema.json so far. To be added: spatial and spatial_uri
* dct:publisher: Information is taken from the config file (see above), not giver for each dataset
* dct:license: In default CKAN this is given on dataset level, but in DCAT-AP it is given on distribution level. We copy the info from the dataset to the distribution

The following fields have range dcat:dataset, and should be mapped using CKAN's relationship ( http://docs.ckan.org/en/latest/api/index.html#ckan.logic.action.create.package_relationship_create ):
* dct:hasVersion
* dct:isVersionOf
* dct:source
* dct:references
* dct:isReferencedBy
* dct:isPartOf
* dct:hasPart
* dct:requires
* dct:isRequiredBy
* dct:replaces
* dct:isReplacedBy

Resources (= distributions in CKAN): 

* DCAT-AP and DCAT-AP-NO fields not included in scheme file yet

## TODO

* Add DCAT-AP-NO fields for Resources
* Compare field formats in dcat_ap_no_schema.json and profiles.py (done, but another check won't hurt)
* Selection lists for controlled vocabs (like Frequency)
* Figure out selection list for huge controlled vocabs
* Figure out fields with range dcat:dataset
* Make a light version of dcat_ap_no_schema.json, which doesn't include optional fields which we don't intend to use
* Go through all changes in code that are relevant to `ckanext-dcat`, check which ones should be contributed back
* On brief testing, it seemed that license = "Annet (åpen)" wasn't listed for distribution, but when I changed to a CC license, it appeared. Test with various licenses!
* Add help text showing which fields are expected to be URLs