# ckanext-dcat_ap_no

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

The field 'dcat_ap_no_comment' is used to list the field's corresponding URI in the standard. It will not be displayed, and is just used as a comment for information.

For most of the fields, we can't support cardinality greater than 1.

Datasets: The following fields from DCAT-AP-NO has currently *not* been mapped in dcat_ap_no_schema.json:

* dcat:contactPoint: 
 * CKAN field maintainer OR author should be mapped to it
 * Only email is given as contact info, additional contact info should be added
* dcat:distribution: We'll using Resource for this
* dct:conformsTo has been mapped, but maybe we should use Related for it instead
* foaf:page: ditto
* dct:hasVersion: Not mapped, should use Related
* dct:isVersionOf: ditto
* dct:relation: ditto
* adms:sample: Not mapped, should use Resource
* dct:source: Not mapped, should use Related
* dct:temporal: Has been mapped, but have used separate fields for start date and end date
* dct:references: Not mapped, should use Related
* dct:isReferencedBy: ditto
* dct:isPartOf: ditto
* dct:hasPart: ditto
* dct:requires: ditto
* dct:isRequiredBy: ditto
* dct:replaces: ditto
* dct:isReplacedBy: ditto

Resources (= distributions in CKAN): 

* Not mapped yet.