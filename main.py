import cv2

image_path = 'faker.jpg'
image_bgr = cv2.imread(image_path)

image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagen en color', image_bgr)
cv2.imshow('Imagen en escala de grises', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

