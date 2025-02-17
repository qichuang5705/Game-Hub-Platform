from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import asset, Purchase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

user = get_user_model()

class AssetModelTest(TestCase):
    def setUp(self):
        self.user = user.objects.create_user(
            username='testuser',
            password='pass')
        self.asset = asset.objects.create(
            price=100,
            type='3D Model',
            description='A high-quality 3D model',
            quantifier=10,
            title='3D Gold',
            create_date=None,
            thumnail=SimpleUploadedFile(
                name='test_image.jpg', 
                content=b'', 
                content_type='image/jpeg'),
            user=self.user
        )
    
    def test_asset_creation(self):
        self.assertEqual(self.asset.price, 100)
        self.assertEqual(self.asset.type, '3D Model')
        self.assertEqual(self.asset.user, self.user)
        self.assertIsNotNone(self.asset.create_date)
    
    def test_asset_missing_title(self):
        with self.assertRaises(IntegrityError):
            asset.objects.create(
                price=50, 
                type='Texture', 
                description='Missing title',
                quantifier=5, 
                create_date=None,
                user=self.user)
    
    def test_asset_negative_price(self):
        with self.assertRaises(Exception):
            asset.objects.create(
                price=-10, 
                type='Invalid', 
                description='Negative price', 
                quantifier=1, 
                title='Invalid Asset',
                create_date=None,
                user=self.user)

class PurchaseModelTest(TestCase):
    def setUp(self):
        self.user = user.objects.create_user(username='buyer', password='buyerpass')
        self.asset = asset.objects.create(
            price=100,
            type='Sound Effect',
            description='A high-quality sound effect',
            quantifier=5,
            title='Explosion Sound',
            create_date=None,
            thumnail=SimpleUploadedFile(
                name='sound.jpg', 
                content=b'',
                content_type='image/jpeg'),
            user=self.user
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
        with self.assertRaises(ValidationError):
            invalid_purchase=Purchase(
                user=self.user,
                asset=self.asset,
                payment_method='bitcoin'   
            )
            invalid_purchase.full_clean()


