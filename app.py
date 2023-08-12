import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS
import python_actr
from python_actr import *
print("as900000000000000000")
#log=log(html=True)

import logging
import unittest

import HTMLTestRunner

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class BasicTestCase(unittest.TestCase):
    def test_one(self):
        logger.info('Test message 1!')
        self.assertEqual(1, 1)

    def test_two(self):
        """Extended description"""
        logger.error('Test message 1!')
        self.assertEqual(2, 2)


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr)

    with open('report.html', 'w') as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=report_file,
            title='Test Report',
            description='Regression Test Suite',
            verbosity=3,
            logger=logger
        )

        suite = unittest.TestLoader().loadTestsFromTestCase(BasicTestCase)

        result = runner.run(suite)
        print(result)
class MyEnvironment(Model):
    pass

#####
# create an act-r agent

class MyAgent(ACTR):
    
    focus=Buffer()
    focus.set('sandwich bread')
    #log.as0=111
    #log.as2="aaa"
    def bread_bottom(focus='sandwich bread'):     # if focus buffer has this chunk then....
        print("I have a piece of bread")           # print
        focus.set('sandwich cheese')              # change chunk in focus buffer

    def cheese(focus='sandwich cheese'):          # the rest of the productions are the same
        print ("ended")    # but carry out different actions
        focus.set('stop')
    def stop_production(focus='stop'):
        self.stop()                        # stop the agent
##
##    def ham(focus='sandwich ham'):
##        print "I have put  ham on the cheese"
##        focus.set('sandwich bread_top')
##
##    def bread_top(focus='sandwich bread_top'):
##        print "I have put bread on the ham"
##        print "I have made a ham and cheese sandwich"
##        focus.set('stop')   
##

print("as800000000000000000")

def main():
    st.title(log.aa)

    with st.sidebar:
        st.header("Configuration")
        api_options = ("echarts", "pyecharts")
        selected_api = st.selectbox(
            label="Choose your preferred API:",
            options=api_options,
        )

        page_options = (
            list(ST_PY_DEMOS.keys())
            if selected_api == "pyecharts"
            else list(ST_DEMOS.keys())
        )
        selected_page = st.selectbox(
            label="as label",
            options=page_options,
        )
        demo, url = (
            ST_DEMOS[selected_page]
            if selected_api == "echarts"
            else ST_PY_DEMOS[selected_page]
        )

        if selected_api == "echarts":
            st.caption(
                """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html, 
            by copying/formattting the 'option' json object into st_echarts.
            Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
            )
        if selected_api == "pyecharts":
            st.caption(
                """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
            by copying the pyecharts object into st_pyecharts. 
            Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts and st_pyecharts is different."""
            )

    demo()
    print("as700000000000000000")

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))
    st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    print("main000000")

    st.set_page_config(
        page_title="aso title", page_icon=":chart_with_upwards_trend:"
    )
    print("main2")

    main()
    tim=MyAgent()                              # name the agent
    subway=MyEnvironment()                     # name the environment
    subway.agent=tim                           # put the agent in the environment
    ##ccm.log_everything(subway)                 # print out what happens in the environment

    subway.run()                               # run the environment
    print("run")
    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
            unsafe_allow_html=True,
        )
print("end")
