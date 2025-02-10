from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Asset

class AssetAPITest(APITestCase):
    def setUp(self):
        """Tạo dữ liệu mẫu"""
        self.asset = Asset.objects.create(
            name="API Test Asset",
            description="Testing API",
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        )

<<<<<<< HEAD
    def test_get_asset_list(self):
        """Kiểm tra API trả về danh sách tài sản"""
        response = self.client.get("/api/assets/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_asset(self):
        """Kiểm tra API tạo mới tài sản"""
        data = {
            "name": "New Asset",
            "description": "New Asset Description",
        }
        response = self.client.post("/api/assets/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
=======
#ctrl + f để tìm kiếm nhanh
print("ss")
print("ss")
print("ss")
print("ss")
print("ss")
print("ss")
print("ss")
print("ss")
>>>>>>> 8e03684fd4b6395ab5b2ac817c62b135387b4bc5
