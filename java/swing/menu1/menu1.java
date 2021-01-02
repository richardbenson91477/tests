
import java.awt.event.*;
import javax.swing.*;

public class menu1 extends JFrame implements ActionListener {
    static final long serialVersionUID = 1L;

    JMenuBar menuBar = new JMenuBar ();
    JMenu menu = new JMenu ("File");
    JMenu menu1 = new JMenu ("Edit");
    JMenuItem item1 = new JMenuItem ("New");
    JMenuItem item2 = new JMenuItem ("Open");
    JButton myButton=new JButton ("Click");

    public menu1 () {
        setJMenuBar (menuBar);
        setVisible (true);
        setSize (400, 200);
        menuBar.add (menu);
        menuBar.add (menu1);
        item1.addActionListener (this);
        myButton.addActionListener (this);
        menu.add (item1);
        menu.add (item2);
        JPanel panel=new JPanel ();
        setTitle ("JLabel Font Change");
        setDefaultCloseOperation (EXIT_ON_CLOSE);
        getContentPane ().add (panel);
        panel.setLayout (null);
        myButton.setBounds (95, 55, 90, 50);
        panel.add (myButton);
        setVisible (true);
    }

    public void actionPerformed (ActionEvent e) {
        if (e.getSource () == item1) {
            System.out.println ("\n");
            System.out.println ("You have Clicked on JMenu item");
            System.out.println ("Put Your Menu Item Action Condition here");
        }
        else if (e.getSource () == myButton) {
            System.out.println ("\n");
            System.out.println ("You have Clicked on Button item");
            System.out.println ("Put Your Button Action Condition here");
        }
    }

    public static void main (String[] args) {
        new menu1 ();
    }
}

