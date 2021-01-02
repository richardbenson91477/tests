import java.awt.FlowLayout;
import javax.swing.*;
 
public class swing2 {
    public static void main (String[] args) {
        var f = new JFrame ("Hello, !");
        f.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        f.setLayout (new FlowLayout ());
        f.add (new JLabel ("Hello, world!"));
        f.add (new JButton ("Press me!"));
        f.pack ();
        f.setVisible (true);
    }
}

