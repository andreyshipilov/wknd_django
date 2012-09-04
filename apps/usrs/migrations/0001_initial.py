# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Profile'
        db.create_table('usrs_profile', (
            ('user', self.gf('annoying.fields.AutoOneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('user_type', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('manager_of', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wknd.Place'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('usrs', ['Profile'])

        # Adding M2M table for field favourite_places on 'Profile'
        db.create_table('usrs_profile_favourite_places', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['usrs.profile'], null=False)),
            ('place', models.ForeignKey(orm['wknd.place'], null=False))
        ))
        db.create_unique('usrs_profile_favourite_places', ['profile_id', 'place_id'])


    def backwards(self, orm):
        
        # Deleting model 'Profile'
        db.delete_table('usrs_profile')

        # Removing M2M table for field favourite_places on 'Profile'
        db.delete_table('usrs_profile_favourite_places')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 5, 5, 23, 25, 870000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 5, 5, 23, 25, 870000)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'usrs.profile': {
            'Meta': {'object_name': 'Profile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'favourite_places': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'usrs_profile_related'", 'blank': 'True', 'to': "orm['wknd.Place']"}),
            'manager_of': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wknd.Place']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('annoying.fields.AutoOneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'user_type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'})
        },
        'wknd.place': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'coords_lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '17', 'blank': 'True'}),
            'coords_lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '17', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['usrs']
