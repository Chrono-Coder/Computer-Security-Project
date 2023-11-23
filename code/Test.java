public class Test {
    static {
        System.loadLibrary("opencv_info");
    }

    public static native void JNI_OnLoad();

    public static void main(String[] args) {
        System.out.print("RUNNING");
        //JNI_OnLoad();
    }
}
