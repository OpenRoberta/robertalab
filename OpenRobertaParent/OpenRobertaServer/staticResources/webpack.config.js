const path = require('path'),
    webpack = require('webpack'),
    basePath = path.resolve(__dirname) + '/',
    publicPath = '/bundle/',
    distPath = path.resolve(basePath, '../target/js' + publicPath) + '/',
    sourcePath = path.resolve(basePath, 'js') + '/';

module.exports = function(env) {
    return {
        target: 'web',
        plugins: [
            new webpack.ProvidePlugin({
                goog: ['blockly', 'goog'],
                Blockly: ['blockly', 'Blockly']
            })],
        entry: 'main.js',
        output: {
            filename: 'roberta.min.js',
            path: distPath,
            publicPath: publicPath
        },
        devtool: 'eval-source-map',
        module: {
            rules: [
                {
                    test: /blockly_compressed\.js$/,
                    use: {
                        loader: 'exports-loader',
                        options: {
                            goog: 'goog',
                            Blockly: 'Blockly'
                        }
                    }
                },
                {
                    test: /blockly/,
                    exclude: /blockly_compressed\.js$/,
                    use: [
                        {
                            loader: 'exports-loader',
                            options: {
                                Blockly: true
                            }
                        }
                    ]
                },
                {
                    test: /libs/,
                    exclude: /jquery\-(?:\d+\.)+(?:min\.)?js$/,
                    use: {
                        loader: 'imports-loader',
                        options: {
                            'this': '>window',
                            'window': '>this.window',
                            '$': 'jquery',
                            'window.jQuery': 'jquery',
                            jQuery: 'jquery'
                        }
                    }
                },
                {
                    resource: sourcePath + 'libs/sound/volume-meter',
                    use: {
                        loader: 'exports-loader',
                        options: {
                            Volume: 'createVolumeMeter'
                        }
                    }
                }
            ]
        },
        resolveLoader: {
            modules: [path.resolve(basePath, 'node_modules') + '/']
        },
        resolve: {
            modules: [sourcePath],
            alias: {
                'blockly' : (sourcePath + '../blockly/blockly_compressed'),
                'blocks' : (sourcePath + '../blockly/blocks_compressed'),
                'blocks-msg' : (sourcePath + '../blockly/msg/js/en'),
                'msgfiles': (sourcePath + '../blockly/msg/js'),
                'bootstrap' : (sourcePath + 'libs/bootstrap/bootstrap-3.3.1-dist/dist/js/bootstrap.min'),
                'bootstrap-table' : (sourcePath + 'libs/bootstrap/bootstrap-3.3.1-dist/dist/js/bootstrap-table.min'),
                'bootstrap-tagsinput' : (sourcePath + 'libs/bootstrap/bootstrap-3.3.1-dist/dist/js/bootstrap-tagsinput.min'),
                'bootstrap.wysiwyg' : (sourcePath + 'libs/bootstrap/bootstrap-3.3.1-dist/dist/js/bootstrap-wysiwyg.min'),
                'datatables' : (sourcePath + 'libs/jquery/jquery.dataTables.min'),
                'enjoyHint' : (sourcePath + 'libs/enjoyHint/enjoyhint'),
                'jquery' : (sourcePath + 'libs/jquery/jquery-3.3.1.min'),
                'jquery-cookie' : (sourcePath + 'libs/jquery/jquery.cookie-1.4.1'),
                'jquery-scrollto' : (sourcePath + 'libs/jquery/jquery.scrollTo-2.1.2.min'),
                'jquery-validate' : (sourcePath + 'libs/jquery/jquery.validate-1.17.0.min'),
                'jquery-hotkeys' : (sourcePath + 'libs/jquery/jquery.hotkeys-0.2.0'),
                'slick' : (sourcePath + 'libs/slick/slick.min'),
                'prettify' : (sourcePath + 'libs/code-prettify/prettify'),
                'socket.io' : (sourcePath + 'libs/socket.io/socket.io'),
                'volume-meter' : (sourcePath + 'libs/sound/volume-meter'),

                'confDelete.controller' : (sourcePath + 'app/roberta/controller/confDelete.controller'),
                'configuration.controller' : (sourcePath + 'app/roberta/controller/configuration.controller'),
                'configuration.model' : (sourcePath + 'app/roberta/models/configuration.model'),
                'confList.controller' : (sourcePath + 'app/roberta/controller/confList.controller'),
                'confList.model' : (sourcePath + 'app/roberta/models/confList.model'),
                'cookieDisclaimer.controller' : (sourcePath + 'app/roberta/controller/cookieDisclaimer.controller'),
                'galleryList.controller' : (sourcePath + 'app/roberta/controller/galleryList.controller'),
                'guiState.controller' : (sourcePath + 'app/roberta/controller/guiState.controller'),
                'guiState.model' : (sourcePath + 'app/roberta/models/guiState.model'),
                'import.controller' : 'app/roberta/controller/import.controller',
                'language.controller' : (sourcePath + 'app/roberta/controller/language.controller'),
                'logList.controller' : (sourcePath + 'app/roberta/controller/logList.controller'),
                'logList.model' : (sourcePath + 'app/roberta/models/logList.model'),
                'menu.controller' : (sourcePath + 'app/roberta/controller/menu.controller'),
                'progCode.controller' : (sourcePath + 'app/roberta/controller/progCode.controller'),
                'progDelete.controller' : (sourcePath + 'app/roberta/controller/progDelete.controller'),
                'progHelp.controller' : (sourcePath + 'app/roberta/controller/progHelp.controller'),
                'progInfo.controller' : (sourcePath + 'app/roberta/controller/progInfo.controller'),
                'progRun.controller' : (sourcePath + 'app/roberta/controller/progRun.controller'),
                'progList.controller' : (sourcePath + 'app/roberta/controller/progList.controller'),
                'progList.model' : (sourcePath + 'app/roberta/models/progList.model'),
                'program.controller' : (sourcePath + 'app/roberta/controller/program.controller'),
                'program.model' : (sourcePath + 'app/roberta/models/program.model'),
                'progShare.controller' : (sourcePath + 'app/roberta/controller/progShare.controller'),
                'progSim.controller' : (sourcePath + 'app/roberta/controller/progSim.controller'),
                'robot.controller' : (sourcePath + 'app/roberta/controller/robot.controller'),
                'robot.model' : (sourcePath + 'app/roberta/models/robot.model'),
                'tour.controller' : (sourcePath + 'app/roberta/controller/tour.controller'),
                'user.controller' : (sourcePath + 'app/roberta/controller/user.controller'),
                'user.model' : (sourcePath + 'app/roberta/models/user.model'),
                'rest.robot' : (sourcePath + 'app/roberta/rest/robot'),
                'socket.controller' : (sourcePath + 'app/roberta/controller/socket.controller'),

                'simulation.constants' : (sourcePath + 'app/simulation/simulationLogic/constants'),
                'simulation.math' : (sourcePath + 'app/simulation/simulationLogic/math'),
                'simulation.program.builder' : (sourcePath + 'app/simulation/robertaLogic/program.builder'),
                'simulation.program.eval' : (sourcePath + 'app/simulation/robertaLogic/program.eval'),
                'simulation.robot' : (sourcePath + 'app/simulation/simulationLogic/robot'),
                'simulation.robot.draw' : (sourcePath + 'app/simulation/simulationLogic/robot.draw'),
                'simulation.robot.mbed' : (sourcePath + 'app/simulation/simulationLogic/robot.mbed'),
                'simulation.robot.calliope' : (sourcePath + 'app/simulation/simulationLogic/robot.calliope'),
                'simulation.robot.calliope2016' : (sourcePath + 'app/simulation/simulationLogic/robot.calliope2016'),
                'simulation.robot.calliope2017' : (sourcePath + 'app/simulation/simulationLogic/robot.calliope2017'),
                'simulation.robot.microbit' : (sourcePath + 'app/simulation/simulationLogic/robot.microbit'),
                'simulation.robot.math' : (sourcePath + 'app/simulation/simulationLogic/robot.math'),
                'simulation.robot.rescue' : (sourcePath + 'app/simulation/simulationLogic/robot.rescue'),
                'simulation.robot.roberta' : (sourcePath + 'app/simulation/simulationLogic/robot.roberta'),
                'simulation.robot.simple' : (sourcePath + 'app/simulation/simulationLogic/robot.simple'),
                'simulation.robot.ev3' : (sourcePath + 'app/simulation/simulationLogic/robot.ev3'),
                'simulation.robot.nxt' : (sourcePath + 'app/simulation/simulationLogic/robot.nxt'),
                'simulation.scene' : (sourcePath + 'app/simulation/simulationLogic/scene'),
                'simulation.simulation' : (sourcePath + 'app/simulation/simulationLogic/simulation'),

                'comm' : (sourcePath + 'helper/comm'),
                'log' : (sourcePath + 'helper/log'),
                'message' : (sourcePath + 'helper/msg'),
                'util' : (sourcePath + 'helper/util'),
                'wrap' : (sourcePath + 'helper/wrap'),

                'robertaLogic.actors' : (sourcePath + 'app/simulation/robertaLogic/actors'),
                'robertaLogic.constants' : (sourcePath + 'app/simulation/robertaLogic/constants'),
                'robertaLogic.memory' : (sourcePath + 'app/simulation/robertaLogic/memory'),
                'robertaLogic.motor' : (sourcePath + 'app/simulation/robertaLogic/motor'),
                'robertaLogic.program' : (sourcePath + 'app/simulation/robertaLogic/program'),
                'robertaLogic.timer' : (sourcePath + 'app/simulation/robertaLogic/timer'),
                'robertaLogic.gyro' : (sourcePath + 'app/simulation/robertaLogic/gyro')
            }
        }
    };
}();