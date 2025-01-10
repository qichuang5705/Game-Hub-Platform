export const emailInput = document.getElementById('exampleInputEmail');
export const passwordInput = document.getElementById('exampleInputPassword');
export const submitButton = document.getElementById('submitButton');

export const toggleSubmitButton = () => {
    console.log('vaooooo')
  const email = emailInput.value.trim();
  const password = passwordInput.value.trim();

  // Enable the submit button only if both email and password are not empty
  submitButton.disabled = !(email && password);
}

export const handleFormSubmit = async(event)=> {
  event.preventDefault(); // Ngăn chặn hành động mặc định của form (reload trang)

  // Lấy dữ liệu từ các input
  const email = emailInput.value;
  const password = passwordInput.value;

  try {
    console.log('Email:', email);
    console.log('Password:', password);

    // Tạm dừng 500ms trước khi chuyển trang
    setTimeout(() => {
      //window.location.href = '/pages/register.html';
    }, 500);
  } catch (error) {
    console.error('Error:', error);
    alert('An error occurred. Please try again.');
  }
}
