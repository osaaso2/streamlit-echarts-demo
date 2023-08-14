import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS
from python_actr import *
print("as900000000000000000")
#logger=log(html=True)
#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
import unittest
import sys
from qiskit import *
import pylatexenc
from qiskit.circuit import Parameter, QuantumCircuit

x = Parameter('x')
y = Parameter('y')

circuit = QuantumCircuit(2)
circuit.rx(x, 1)
circuit.cx(1, 0)
circuit.ry(-2*y, 0)
#circuit.draw("mpl")

log.action1=1

#log=log()
log.action1=10
as2=10

class ForcedChoiceEnvironment(Model):
  # this is an action that can be taken by the agent in the environment
  def press(self,letter):     # 'self' refers to the thing we are currently
                              #  of defining.  In this case, the environment

    if letter=='A':
      log.action1+=10    # here we record what letter was pressed

      self.reward=1      # if it was 'A', we set the reward to one.  
    else:
      self.reward=0      # otherwise, set it to zero.


# This defines a simple agent.  We will examine this in more detail in the
#  tutorials on creating models
class SimpleModel(Model):
  def start(self):

    while True:               # repeat the following forever
      self.parent.press('A')
      yield 2                 # wait for 1 second before continuing


# Now that the agent and the environment have been defined, we can create
#  one of each, connect them together, and run the simulation.      
env=ForcedChoiceEnvironment()   # create the environment
model=SimpleModel()             # create the agent
env.agent=model                 # put the agent in the environment
log_everything(env)
env.run(8)  
print("act1",log.action1)

def main():
    st.title("Streamlit ECharts Demo")

    with st.sidebar:
        st.header("Configuration")
        api_options = ("echarts", "pyecharts")
        selected_api = st.selectbox(
            label=circuit.draw() #str(log.action1),
            options=api_options,
        )

        page_options = (
            list(ST_PY_DEMOS.keys())
            if selected_api == "pyecharts"
            else list(ST_DEMOS.keys())
        )
        selected_page = st.selectbox(
            label="Choose an example",
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

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))
    st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
    )
    main()
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
