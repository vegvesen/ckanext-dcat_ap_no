# ckanext-dcat_ap_no

NB! This is still a work in progress, not ready for use yet!

This is a collection of stuff needed to make CKAN conform to DCAT-AP-NO, the Norwegian adaption of the DCAT-AP standard. (It's compatible with DCAT-AP, but has a few additional fields.) It can be found here: https://doc.difi.no/dcat-ap-no/

## Requirements

Install the plugins `ckanext-dcat` and `ckanext-scheming` and configure them accordingly.

#### Note!


Until `ckanext-dcat` has merged [PR#66](https://github.com/ckan/ckanext-dcat/pull/66) you have to install from the fork using
    
    (pyenv) $ pip install -e git+https://github.com/vegvesen/ckanext-dcat.git@feature/dcat-ap11#egg=ckanext-dcat

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

## Additional information

### Schema specified in dcat_ap_no_schema.json

The field dcat_ap_no_comment is used to list the field's corresponding URI in the standard. It will not be displayed, and is just used as a comment for information.

For most of the fields, we can't support cardinality greater than 1.

#### Datasets
The following fields from DCAT-AP-NO has currently *not* been mapped in dcat_ap_no_schema.json:

* dcat:contactPoint: 
 * Only email is given as contact info, additional contact info should be added
* dcat:distribution: Resource is used for this
* adms:sample: Not mapped, should use Resource with a new field indicating that this is an example
* dct:relation ?

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

There used to be a CKAN field for apps, articles etc, which might be useful for some of the fields which are links. 
TODO: Check what happened to it!

Resources (= distributions in CKAN): 

* Not mapped yet.