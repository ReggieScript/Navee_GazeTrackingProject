{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Demonstration of the GazeTracking library.\n",
    "Check the README.md for complete documentation.\n",
    "\"\"\"\n",
    "\n",
    "import cv2\n",
    "from gaze_tracking import GazeTracking\n",
    "\n",
    "gaze = GazeTracking()\n",
    "webcam = cv2.VideoCapture(0)\n",
    "\n",
    "while True:\n",
    "    # We get a new frame from the webcam\n",
    "    _, frame = webcam.read()\n",
    "\n",
    "    # We send this frame to GazeTracking to analyze it\n",
    "    gaze.refresh(frame)\n",
    "\n",
    "    frame = gaze.annotated_frame()\n",
    "    text = \"\"\n",
    "\n",
    "    if gaze.is_blinking():\n",
    "        text = \"Blinking\"\n",
    "    elif gaze.is_right():\n",
    "        text = \"Looking right\"\n",
    "    elif gaze.is_left():\n",
    "        text = \"Looking left\"\n",
    "    elif gaze.is_center():\n",
    "        text = \"Looking center\"\n",
    "\n",
    "    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)\n",
    "\n",
    "    left_pupil = gaze.pupil_left_coords()\n",
    "    right_pupil = gaze.pupil_right_coords()\n",
    "    cv2.putText(frame, \"Left pupil:  \" + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)\n",
    "    cv2.putText(frame, \"Right pupil: \" + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)\n",
    "\n",
    "    cv2.imshow(\"Demo\", frame)\n",
    "\n",
    "    if cv2.waitKey(1) == 27:\n",
    "        break\n",
    "   \n",
    "webcam.release()\n",
    "cv2.destroyAllWindows()\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
