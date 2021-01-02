#include <gtk/gtk.h>

G_MODULE_EXPORT void bhandler (GtkButton *b, gpointer data) {
	printf ("Hello, world!\n");
}

int main (int argc, char *argv[]) {
	GtkWidget *wgt_win1, *wgt_but1;
	GtkBuilder *builder;

	gtk_init (&argc, &argv);

	builder = gtk_builder_new ();
	gtk_builder_add_from_file (builder, "cgtk3.glade", NULL);
	gtk_builder_connect_signals (builder, NULL);

	wgt_win1 = GTK_WIDGET(gtk_builder_get_object (builder, "window1"));
	wgt_but1 = GTK_WIDGET(gtk_builder_get_object (builder, "button1"));

	g_signal_connect (wgt_but1, "clicked", G_CALLBACK(bhandler), NULL);

	g_signal_connect (G_OBJECT(wgt_win1), "destroy", G_CALLBACK(gtk_main_quit), NULL);

	g_signal_connect (G_OBJECT(wgt_win1), "delete-event",
        G_CALLBACK(gtk_main_quit), NULL);

	gtk_widget_show (wgt_win1);

	gtk_main ();
	return 0;
}

