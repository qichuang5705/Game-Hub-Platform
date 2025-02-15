from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import asset, Purchase
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

User = get_user_model()

class AssetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.asset = asset.objects.create(
            price=100,
            type='3D Model',
            description='A high-quality 3D model',
            quantifier=10,
            title='3D Dragon',
            thumnail=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            User=self.user
        )
    
    def test_asset_creation(self):
        self.assertEqual(self.asset.price, 100)
        self.assertEqual(self.asset.type, '3D Model')
        self.assertEqual(self.asset.User, self.user)
    
    def test_asset_missing_title(self):
        with self.assertRaises(Exception):
            asset.objects.create(price=50, type='Texture', description='Missing title', quantifier=5, User=self.user)
    
    def test_asset_negative_price(self):
        with self.assertRaises(Exception):
            asset.objects.create(price=-10, type='Invalid', description='Negative price', quantifier=1, title='Invalid Asset', User=self.user)

class PurchaseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='buyer', password='buyerpass')
        self.asset = asset.objects.create(
            price=50,
            type='Sound Effect',
            description='A high-quality sound effect',
            quantifier=5,
            title='Explosion Sound',
            thumnail=SimpleUploadedFile(name='sound.jpg', content=b'', content_type='image/jpeg'),
            User=self.user
        )
        self.purchase = Purchase.objects.create(
            user=self.user,
            asset=self.asset,
            payment_method='paypal'
        )
    
    def test_purchase_creation(self):
        self.assertEqual(self.purchase.user, self.user)
        self.assertEqual(self.purchase.asset, self.asset)
        self.assertEqual(self.purchase.payment_method, 'paypal')
    
    def test_purchase_invalid_payment_method(self):
        with self.assertRaises(Exception):
            Purchase.objects.create(user=self.user, asset=self.asset, payment_method='bitcoin')


