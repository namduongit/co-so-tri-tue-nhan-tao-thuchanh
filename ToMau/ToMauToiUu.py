'''
Tính bậc của tất cả các đỉnh
while (còn đỉnh có bậc lớn hơn 0)
{
	-Tìm đỉnh(chưa được tô) có bậc lớn nhất. Chẳng hạn đó là đỉnh i0.
	-Tìm màu để tô đỉnh i0 là màu nhỏ nhất trong danh sách các màu còn lại có
	thể tô cho đỉnh i0. Chẳng hạn đó là màu j.
	-Ngăn cấm việc tô màu j cho các đỉnh kề với đỉnh i0.
	-Tô màu đỉnh i0 là j.
	-Gán bậc của đỉnh được tô bằng 0, các đỉnh kề với đỉnh được tô có bậc giảm
	đi 1 đơn vị.
}
Sau khi kết thúc vòng lập trên có thể còn đỉnh chưa được tô nhưng tất cả các 
đỉnh lúc này đều đã có bậc bằng 0 – nghĩa là không thể hạ bậc được nữa. 
Khi đó màu của các đỉnh chưa được tô chính là màu nhỏ nhất hợp lệ trong 
danh sách màu của đỉnh đó.

'''