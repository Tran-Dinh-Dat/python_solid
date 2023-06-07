# Nguyên tắc SOLID

### Nguyên tắc Đơn trách nhiệm (Single Responsibility Principle - SRP): 
Một class nên chỉ có một lý do để thay đổi. Điều này đảm bảo rằng mỗi class chỉ nên có một trách nhiệm cụ thể và không bị quá tải chức năng.

### Nguyên tắc Mở rộng đóng gói (Open-Closed Principle - OCP):
Mã nguồn nên được mở để mở rộng (thêm chức năng mới) nhưng đóng lại để sửa đổi. Điều này đảm bảo rằng khi cần thay đổi hành vi của một class, chúng ta nên mở rộng class đó bằng cách kế thừa hoặc triển khai các interface, mà không làm thay đổi mã nguồn gốc.

### Nguyên tắc Substitution (Liskov Substitution Principle - LSP):
Các đối tượng của một lớp con có thể được sử dụng thay thế cho các đối tượng của lớp cha mà không làm thay đổi tính đúng đắn của chương trình. Điều này đảm bảo rằng các lớp con phải tuân thủ các ràng buộc của lớp cha và không làm thay đổi hành vi của lớp cha.

### Nguyên tắc Tách biệt (Interface Segregation Principle - ISP):
Nên ưu tiên việc phân chia các interface thành các phần nhỏ hơn, cụ thể, hơn là một interface lớn chứa nhiều phương thức. Điều này giúp tránh việc các class phụ thuộc vào các phương thức không liên quan và giảm thiểu sự phụ thuộc không cần thiết.

### Nguyên tắc Đảo ngược sự phụ thuộc (Dependency Inversion Principle - DIP):
Các module cấp cao không nên phụ thuộc vào các module cấp thấp. Cả hai nên phụ thuộc vào các abstraction. Điều này đảm bảo rằng mã nguồn không phụ thuộc vào các module cụ thể mà thay vào đó phụ thuộc vào các abstraction, tạo ra sự linh hoạt và dễ dàng thay đổi.