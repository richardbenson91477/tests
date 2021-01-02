
public class try1 {
    public static void main (String [] args) {
        int [] x = new int [1];
        try {
            x [3] = 100; 
        }
        catch (Exception exc) {
            var newEx = new Exception ("Error at:" + new java.util.Date() + "",
                exc);
            newEx.printStackTrace ();
            System.out.println ("Hello, ");
        }
        finally {
            System.out.println ("world!");
        }
    }
}

