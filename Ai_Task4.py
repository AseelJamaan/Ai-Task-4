import cv2

# فتح الكاميرا
cap = cv2.VideoCapture(0)

# تحديد المتتبع (Tracker)
tracker = cv2.legacy.TrackerCSRT_create()

# قراءة الإطار الأول من الفيديو
ret, frame = cap.read()

# اختيار المنطقة التي تحتوي على الجسم الذي تريد تتبعه (يمكنك تحديد مستطيل يدويًا)
bbox = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # تحديث المتتبع
    success, bbox = tracker.update(frame)
    
    if success:
        # رسم المستطيل حول الجسم المتتبع
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 3)
    else:
        cv2.putText(frame, "Lost Track", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # عرض الفيديو مع المتابعة
    cv2.imshow("Object Tracking", frame)
    
    # الخروج من الحلقة عند الضغط على "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# إغلاق الكاميرا
cap.release()
cv2.destroyAllWindows()
