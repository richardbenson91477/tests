
//class thread1 implements Runnable {
class thread1 extends Thread {
    public static void main (String [] args) {
        var t1 = new thread1 ();

        System.out.println ("press CTRL-4...");
 
        new Thread (t1).start ();
        new Thread (t1).start ();
        System.out.println ("end main");
    }

    public void run () {
        try {
            sleep (1000);
        } catch (InterruptedException e) {
        }
        System.out.println ("run()ning");
    }
}

