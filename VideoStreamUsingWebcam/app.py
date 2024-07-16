from flask import Flask, render_template, Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)# use camera, 0 is by default, open webcame for remote, need its ip& username

def generate_frames():
    while True: #read frame continuously
        #read the camera frame
        success,frame=camera.read()
    
        if not success:
            break
        else:
            detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade=cv2.CascadeClassifier('Haarcascades/haarcascascade_eye.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert To grey scale
            #draw rectangle around each face
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)# bounding box, color-255 rgb, 
                roi_gray=gray[y:y+h,x:x+w] #pick out the face rectangle in a gray scale, use it to 
                roi_color = frame[y:y+h, x:x+w]
                eyes=eye_cascade.detectMultiScale(roi_gray,1.1,3) # eyes have 4 coordinate
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    
            ret,buffer=cv2.imencode('.jpg',frame) #encode image into a memory buffer,  jpg format
            frame=buffer.tobytes() #convert the buffer into bytes
        yield(b'--frame\r\n'
              b'Content-Type:image/jpeg\r\n\r\n'+frame+b'\b\n') #we need to call it continuously, cannot directly return 
        
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__=='__main__':
    app.run(debug=True)