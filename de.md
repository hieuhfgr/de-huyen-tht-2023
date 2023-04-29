**ĐỀ THI TIN HỌC TRẺ 2023 CỦA MỘT HUYỆN NÀO ĐÓ**

---
**Bài 1**: Định nghĩ dãy số $Fibonacci$ là dãy số với hai số đầu tiên là $1,1$. Các số tiếp theo sẽ là tổng của hai số liền kề bên trái nó. 
Ví dụ dãy Fibonacci: $1,1,2,3,5,8,13,21,...$
Hôm nay trên đường đi học về, Tí được crush câu hỏi này thì crush sẽ chấp nhận là ny của cậu. Câu hỏi của crush rằng cho một số tự nhiên $n$ $(0 < n \le 100)$, Hãy kiểm tra xem số đó có phải là số Fibonacci hay không.

**Dữ liệu vào**: nhập từ bàn phím số tự nhiên $n$.

**Dữ liệu ra**: in ra màn hình `YES` nếu $n$ là số Fibonacci, ngược lại in ra `NO`.
## Sample Input 1
```
8
```

## Sample Output 1
```
YES
```
## Sample Input 2
```
9
```

## Sample Output 2
```
NO
```
---
**Bài 2**: Hôm nay trong giờ học toán, Tí đang mơ về cậu và crush năm lớp 6. Lúc đó đang học bài về ước chung lớn nhất và bội chung nhỏ nhất. Crush hỏi Tí rằng: "Nếu tớ cho cậu hai số tự nhiên $a$ và $b$, liệu cậu có thể tìm được bội chung nhỏ nhất của a và b hay không?" Để tạo ấn tượng trong mắt crush, Tí liền nhận lời. Nhưng là học sinh chuyên anh nên cậu không thể nào tìm được. Bạn giúp Tí tán crush nha!

**Dữ liệu vào**: nhập từ bàn phím hai số nguyên $a$ và $b$ $(0 < a,b \le 65000)$.

**Dữ liệu ra**: In ra màn hình gồm 2 dòng:
- **Dòng 1**: in ra bội chung nhỏ nhất của hai số $a, b$.
- **Dòng 2**: rút gọn $\frac{a}{b}$ thành **phân số tối giản** (ghi dưới dạng $a/b$).

## Sample Input 1
```
3 6 
```

## Sample Output 1
```
6
1/2
```
## Sample Input 2
```
9 8
```

## Sample Output 2
```
72
9/8
```

---
**Bài 3**: Trên đường đi Tí có bắt gặp cô bán kem và những cây kem với những chiều cao khác nhau được sắp xếp lộn xộn. Tí là một người ưa hoàn hảo nên cậu muôn sắp xếp những que kem này theo thứ tự giảm dần từ trái sang phải. Vì quá đẹp trai nên cô bán kem đã thưởng cho cậu một que kem nhưng cậu không muốn ăn nên cậu muốn bỏ que kem này vào dãy kem cậu đã sắp xếp.

Túm cái quần lại, cho mảng *h* gồm *n* phần tử. Nhiệm vụ của bạn là sắp xếp mảng *h* theo thứ tự giảm dần. Sau đó chèn phần tử x vào mảng sao cho mảng vẫn đảm bảo giảm dần (lưu ý không được sắp xếp lại mảng!!!).

**Dữ liệu vào**: gồm $(n+2)$ dòng:
- **Dòng đầu**: số tự nhiên $n$ $(0 < n \le 100)$.
- **n dòng tiếp theo**: mỗi dòng là giá trị $h_i$ $(0 < h_i < 10^3)$(dữ liệu đảm bảo không có giá trị nào bị trùng).
- **Dòng cuối**: số tự nhiên $x$ $(0 < x < 10^3)$. là số cần chèn vào mảng.

**Dữ liệu ra**: Gồm 2 dòng:
- **Dòng 1**: Mảng $h$ sau khi sắp xếp tăng dần (chưa chèn phần tử $x$).
- **Dòng 2**: mảng $h$ sau khi chèn phần tử $x$.

# Sample input
```
3
2
3
1
4
```
# Sample output
```
3 2 1
4 3 2 1
```
---
**Bài 4:** Tí yêu toán lớp 1. Hôm nay crush cho cậu một dãy số và đố cậu số nào có tổng chữ số lớn nhất. Mấy bài này quá đơn giản với Tí nên crush lại đố tiếp: "Sau khi tìm được thì cậu hãy in ra số đảo ngược của từng số nhé :3". Mặc dù đơn giản nhưng cậu không biết viết chữ nên nhờ bạn hộ Tí tán crush nhé.

**Dữ liệu vào**: gồm 2 dòng:
- **Dòng 1**: số tự nhiên n là số phần tử trong dãy số $(0 < n \le 100)$.
- **Dòng 2**: n số $a_i$ $(1 \le i \le n)$ $(0 < a_i \le 3200)$.

**Dữ liệu ra**: gòm 2 dòng:
- **Dòng 1**: số có tổng chữ số lớn nhất trong dãy số.
- **Dòng 2**: dãy số sau khi đảo ngược từng số trong mảng.

# Sample input 1
```
3
54 67 132
```
# Sample output 1
```
67
45 76 231
```
---
*Tí là một nhân vật hư cấu!!!*

- From hieuhfgr with love <3
- Thanks Mon for kí hiệu toán học :3
