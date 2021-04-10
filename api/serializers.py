from swapper import load_model
 
from openwisp_users.api.mixins import FilterSerializerByOrgManaged
from openwisp_utils.api.serializers import ValidatedModelSerializer
 
Ca = load_model('pki', 'Ca')
Cert = load_model('pki', 'Cert')


class BaseMeta:
   read_only_fields = ['created', 'modified']


class BaseSerializer(FilterSerializerByOrgManaged, ValidatedModelSerializer):
   pass


class CaSerializer(BaseSerializer):
   class Meta(BaseMeta):
       model = Ca
       fields = '__all__'


class CertSerializer(BaseSerializer):
   class Meta(BaseMeta):
       model = Cert
       fields = '__all__'
