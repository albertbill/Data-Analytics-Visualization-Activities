# Exercise 2 - SPLTV (Sistem Persamaan Linear Tiga Variabel)

## Code

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# soal 1
arrSource = np.array([[1, -2, 1], [3, 1, -2], [7, -6, -1]])
arrResult = np.array([6, 4, 10])
arrTemp = np.linalg.solve(arrSource, arrResult)
print("Nilai x = ", round(arrTemp[0], 1))
print("Nilai y = ", round(arrTemp[1], 1))
print("Nilai z = ", round(arrTemp[2], 1))
# penutup soal 1

# soal 2
plt.figure()

# persamaan 1 => x  - 2y +  z =  6
x1 = np.array([6, 0, 0])
y1 = np.array([0, -3, 0])
z1 = np.array([[0, 0, 6]])
plot1 = plt.subplot(131, projection="3d")
plot1.scatter(x1, y1, z1, c="blue")
plot1.plot_wireframe(x1, y1, z1, facecolor="red", alpha=.3)
plot1.set_title("x - 2y + z = 6")
plot1.set_xlabel("Axis X")
plot1.set_ylabel("Axis Y")
plot1.set_zlabel("Axis Z")

# persamaan 2 => 3x +  y - 2z =  4
x2 = np.array([4.3, 0, 0])
y2 = np.array([0, 4, 0])
z2 = np.array([[0, 0, -2]])
plot2 = plt.subplot(132, projection="3d")
plot2.scatter(x2, y2, z2, c="red")
plot2.plot_wireframe(x2, y2, z2, facecolor="yellow", alpha=.3)
plot2.set_title("3x +  y - 2z =  4")
plot2.set_xlabel("Axis X")
plot2.set_ylabel("Axis Y")
plot2.set_zlabel("Axis Z")

# persamaan 3 => 7x - 6y -  z = 10
x3 = np.array([10/7, 0, 0])
y3 = np.array([0, -10/6, 0])
z3 = np.array([[0, 0, -10]])
plot3 = plt.subplot(133, projection="3d")
plot3.scatter(x3, y3, z3, c="green")
plot3.plot_wireframe(x3, y3, z3, facecolor="blue", alpha=.3)
plot3.set_title("7x - 6y -  z = 10")
plot3.set_xlabel("Axis X")
plot3.set_ylabel("Axis Y")
plot3.set_zlabel("Axis Z")

plt.tight_layout()
plt.show()
# penutup soal 2
```
