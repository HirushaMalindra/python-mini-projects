import cv2
import numpy as np
import math

# Create a variable to track the sweeping angle of the radar
angle = 0

while True:
    # 1. Create a fresh black canvas EVERY frame
    img = np.zeros((500, 500, 3), np.uint8)

    # 2. Draw the static scanner rings
    for r in range(50, 250, 50):
        cv2.circle(img, (250, 250), r, (0, 255, 0), 2)

    # 3. Calculate the sweeping radar line
    # Convert the angle to radians for math.cos and math.sin
    radian = math.radians(angle)

    # Calculate the end point of the line (center is 250,250, radius is 200)
    x = int(250 + 200 * math.cos(radian))
    y = int(250 + 200 * math.sin(radian))

    # Draw the sweeping line
    cv2.line(img, (250, 250), (x, y), (0, 255, 0), 3)

    # 4. Add the text at the bottom
    cv2.putText(img, "SCANNING...", (10, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 5. Show the image
    cv2.imshow("Iris Scanner", img)

    # 6. Increase the angle for the next frame so the line moves
    angle += 2  # Increase this number to make it spin faster!
    if angle >= 360:
        angle = 0

    # 7. Wait 1 millisecond. If the user presses the 'q' key, break the loop to quit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close the window when the loop finishes
cv2.destroyAllWindows()
