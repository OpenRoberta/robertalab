package de.fhg.iais;

import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.net.ServerSocket;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.swing.*;

import org.eclipse.jetty.server.Server;
import org.panda_lang.pandomium.Pandomium;
import org.panda_lang.pandomium.settings.PandomiumSettings;
import org.panda_lang.pandomium.wrapper.PandomiumBrowser;
import org.panda_lang.pandomium.wrapper.PandomiumClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import de.fhg.iais.roberta.main.ServerStarter;
import joptsimple.OptionParser;
import joptsimple.OptionSet;
import joptsimple.OptionSpec;

public class DesktopApp {
    private static final Logger LOG = LoggerFactory.getLogger(DesktopApp.class);

    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(0);
        serverSocket.close();
        String port = String.valueOf(serverSocket.getLocalPort());
        String[] strings =
            new String[] {
                "-d",
                "server.port=" + port,
            };
        List<String> list = new ArrayList<>(Arrays.asList(args));
        list.addAll(Arrays.asList(strings));
        strings = new String[list.size()];
        for ( int i = 0; i < strings.length; i++ ) {
            strings[i] = list.get(i);
        }
        OptionParser parser = new OptionParser();
        OptionSpec<String> defineOpt = parser.accepts("d").withRequiredArg().ofType(String.class);
        OptionSet options = parser.parse(strings);
        List<String> defines = defineOpt.values(options);

        final ServerStarter serverStarter = new ServerStarter(null, defines);
        Server server = serverStarter.start();
        PandomiumSettings settings = PandomiumSettings.getDefaultSettings();
        Pandomium pandomium = new Pandomium(settings);
        pandomium.initialize();

        PandomiumClient client = pandomium.createClient();
        PandomiumBrowser browser = client.loadURL("localhost:" + port);
        JFrame frame = new JFrame();
        frame.getContentPane().add(browser.toAWTComponent(), BorderLayout.CENTER);

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                pandomium.dispose();
                frame.dispose();
            }
        });

        frame.setTitle("OpenRobertaDesktopApp");
        frame.setSize(1380, 760);
        frame.getAccessibleContext();
        frame.setVisible(true);
        server.join();
        System.exit(0);
    }
}