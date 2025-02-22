from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import asset, Purchase 

class AssetModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="testuser")
        self.test_asset = asset.objects.create(
            price=1000,
            type="Digital",
            description="A test asset",
            quantifier=10,
            title="Test Asset",
            User=self.user
        )
    
    def test_asset_creation(self):
        self.assertIsNotNone(self.test_asset.id)
        self.assertEqual(self.test_asset.price, 1000)
        self.assertEqual(self.test_asset.User, self.user)
        self.assertIsNotNone(self.test_asset.create_date)
    
    def test_asset_missing_required_fields(self):
        with self.assertRaises(ValidationError):
            asset_obj = asset(
                price=100,
                type="Physical",
                description="This asset has no title"
            )
            asset_obj.full_clean()

class PurchaseModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="buyer")
        self.test_asset = asset.objects.create(
            price=500,
            type="Service",
            description="A service asset",
            quantifier=5,
            title="Service Asset"
        )
    
    def test_purchase_creation(self):
        purchase = Purchase.objects.create(
            user=self.user,
            asset=self.test_asset,
            payment_method='paypal'
        )
        
        self.assertIsNotNone(purchase.id)
        self.assertEqual(purchase.asset, self.test_asset)
        self.assertEqual(purchase.payment_method, 'paypal')
        self.assertIsNotNone(purchase.purchase_date)
    
    def test_purchase_without_user(self):
        purchase = Purchase.objects.create(
            user=None,
            asset=self.test_asset,
            payment_method='credit_card'
        )
        
        self.assertIsNone(purchase.user)