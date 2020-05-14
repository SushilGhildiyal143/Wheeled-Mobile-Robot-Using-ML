# Control of Wheeled Mobile Robot using Computer Vision
In today’s developing technology,
industries are playing important role for the
betterment of life and society. But in industries
many functions are running under hazardous
conditions, so demand of human free interaction
arises, which can be fulfilled by robotics. In
Chemical, Oil & Gas, Petrochemicals and many
manufacturing industries today we need human
safety on head, and it can be done by robots. This
paper implies such type of mobile robot which can
be used in complex industries. The work is based on
Image processing and Centroid Algorithm. The
physical quantities like (temperature, pressure,
humidity, stress, PH) and leakage of gases and
liquids, fire, spark and many human safety related
things which can be encountered by this mobile
robot. By using this robot, the main achievement is
human safety and simultaneously cost effective,
precision and all far away data can be easily
available through IoT (Cloud). Also, it works
without any disincentive at particular of desired
time in day or night, where particular place requires
physical quantities measurement. In this project the
main components are Controller (Raspberry Pi),
Four DC Motor for each wheel, Pi Camera for
image detection and processing, motor driver logic
and physical quantities sensor.

# METHODOLOGY
To attain this project centroid algorithm is
implemented so that the robot can follow the desired
path. This robot is mainly designed for hazardous
industry purpose. To get the data as well as pictures
at certain time so, by doing the time settings in
robot, it can automatically go and take the data at
that present time. This is accomplished using image
processing, at first video is converted in to frames
with format ‘BGR’ Image. The program is written
in language called Python i.e. high-level language.
Here, robot is design to follow black line, which is
denoted by Image= (0, 0, 0), (75, 75, 75). In GPIO
Board different pins are set for individual motors
that are attached to four wheels. From open
computer vision platform, erode command is used
for noise cancellation. The contour of black line is
detected using ‘find contours’ command [5].
Through this the angle of black line is detected i.e.
when the robot tilts right the angle is towards
negative and when the robot tilts left then the angle
is positive. After finding the contours the centroid
of the black line is measured. Therefore, by taking
centroid as a reference point, the angle is referred as
positive or negative.
The detection of path using camera captures is
shown in image. The bounded rectangle captures
the blackline in the numbers in red color shows the
angle between camera and blackline. When angle is
changed accordingly, output to motors also
changes.


