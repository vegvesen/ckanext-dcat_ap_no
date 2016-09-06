# ckanext-dcat_ap_no

This is a collection of stuff needed to make CKAN conform to the 
norwegian dcat-ap standard.

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
