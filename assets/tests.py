from django.test import TestCase


from django.test import TestCase
from .models import Asset
from django.core.files.uploadedfile import SimpleUploadedFile

class AssetModelTest(TestCase):
    def setUp(self):
        """Tạo dữ liệu mẫu cho kiểm thử"""
        self.asset = Asset.objects.create(
            name="Test Asset",
            description="This is a test asset",
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        )

    def test_asset_creation(self):
        """Kiểm tra xem asset có được tạo thành công không"""
        asset = Asset.objects.get(name="Test Asset")
        self.assertEqual(asset.description, "This is a test asset")

    def test_asset_str_method(self):
        """Kiểm tra phương thức __str__ của model"""
        asset = Asset.objects.get(name="Test Asset")
        self.assertEqual(str(asset), "Test Asset")