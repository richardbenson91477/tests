
public class jni1 {    
    public native void foo ();

    static {
        System.loadLibrary ("foo");
    }        

    public static void main (String [] args) {
        (new jni1 ()).foo ();
        return;
    }
}

