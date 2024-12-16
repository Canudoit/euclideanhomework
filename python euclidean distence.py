import math

# Noktaların tanımlanması
points = [(0, 0), (1, 1), (2, 2), (3, 3)]

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mesafeleri hesaplama ve saklama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonuçları yazdırma
print("Tüm mesafeler:", distances)
print("Minimum mesafe:", min_distance)
