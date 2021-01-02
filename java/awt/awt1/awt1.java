
import java.awt.*;
import java.awt.event.*;

public class awt1 extends Frame implements ActionListener {
    static final long serialVersionUID = 1L;

    Button b1 = new Button ("press me");

    awt1 () {
        super ();
        //setBackground (Color.gray);
        //setLayout (new FlowLayout ());
        setLayout (null);
        setSize (320, 100);
        setTitle ("awt test 1");
 
        addWindowListener (new WindowAdapter () {
            public void windowClosing (WindowEvent event) {
                System.exit (0);
            }
        });

        b1.setLocation (50, 50);
        b1.setSize (96,32);
        b1.addActionListener (this);
        add (b1);
        //pack ();

        setVisible (true);
    }

    public void paint (Graphics g) {
        ((Graphics2D)g).setPaint (Color.blue);
        g.drawString ("text", 10, 50);
    }
    
    public void actionPerformed (ActionEvent e) {
        if (e.getSource () == b1)
            System.out.println ("click");
        
        Graphics g = getGraphics ();
        ((Graphics2D)g).setPaint (Color.red);
        g.drawString ("text", 10, 50);
    }

    public static void main (String [] args) {
        new awt1 ();
    }
}

