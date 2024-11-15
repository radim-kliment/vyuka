## Gradle 

implementation ("org.tensorflow:tensorflow-lite-select-tf-ops:2.16.1")
implementation ("com.google.ai.edge.litert:litert-support")


private fun loadModelFile(): MappedByteBuffer {
    val fileDescriptor = assets.openFd( "converted_model.tflite")
    val inputStream = FileInputStream(fileDescriptor.fileDescriptor)
    val fileChannel = inputStream.channel
    val startOffset = fileDescriptor.startOffset
    val declaredLength = fileDescriptor.declaredLength
    return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength)
}