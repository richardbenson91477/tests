
import java.awt.*;
import java.awt.event.*; 

public class dbuf extends Frame implements MouseMotionListener {
    static final long serialVersionUID = 1L;

    Graphics bufferGraphics = null;
    Image offscreen;
    Dimension dim;
    int curX = 0, curY = 0;
    int resX, resY;

    dbuf () {
        super ();
        setBackground (Color.black);
        setSize (320, 240);
        setTitle ("double buffer test");
        setLayout (null);

        addWindowListener (new WindowAdapter () {
            public void windowClosing (WindowEvent event) {
                System.exit (0);
            }
        });
        addMouseMotionListener (this);

        setVisible (true);
        dim = getSize ();
        this.resX = (int)dim.width;
        this.resY = (int)dim.height;
        offscreen = createImage (this.resX, this.resY);
        bufferGraphics = offscreen.getGraphics ();
    }

    public void paint (Graphics g) {
        if (bufferGraphics != null) {
            bufferGraphics.clearRect (0, 0, this.resX, this.resY);
            bufferGraphics.setColor (Color.red);
            bufferGraphics.drawString ("double-buffered", 10, 64);
            bufferGraphics.fillRect (curX, curY, 32, 32);
            g.drawImage (offscreen, 0, 0, this);
        }
    }

    // override Frame.update to prevent background clear
    public void update (Graphics g) {
        paint (g);
    }
 
    public void mouseMoved (MouseEvent evt) {
        curX = evt.getX ();
        curY = evt.getY ();
        repaint ();
    }

    public void mouseDragged (MouseEvent evt) { }

    public static void main (String [] args) {
        new dbuf ();
    }
}

