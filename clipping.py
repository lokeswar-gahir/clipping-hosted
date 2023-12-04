from polygon_ca import Polygon
from line_ca import Line_clipping
from point_ca import Point_clipping
import streamlit as st

polygon, line, point = st.tabs(["➤ Polygon", "「」Line", "•  Point"])
with polygon:
    st.title("Polygon Clipping", anchor=False)
    st.subheader("Window size", anchor=False)
    st.write("Default window size is (0, 0) and (100, 100)")
    cols = st.columns([3,3])
    with cols[0].expander("Custom window"):
        X_min = st.number_input("X_min", value=0, key=1)
        Y_min = st.number_input("Y_min", value=0, key=2)
        X_max = st.number_input("X_max", value=100, key=3)
        Y_max = st.number_input("Y_max", value=100, key=4)

    p = Polygon((X_min, Y_min), (X_max, Y_max))
    cols[0].subheader("Vertices", anchor=False)
    vertices = st.text_input("Coordinates", placeholder="x1,y1,x2,y2,x3,y3,x4,y4.......")
    if vertices!="":
        vertices = vertices.split(",")
        vertices = list(map(float, vertices))
        if len(vertices)%2!=0:
            st.warning("Enter complete coordinates!!!")
        else:
            st.success("Vertices are set successfully.")
    if st.button("Submit", type="primary", key=5):
        new_vertices=list()
        for i in range(0,len(vertices)-1,2):
            new_vertices.append((vertices[i], vertices[i+1]))
        for v in new_vertices:
            p.set_vertex(v)
        new_coords = p.final_coordinates()
        with st.expander("Outputs"):
            t1,t2,t3,t4,t5 = st.tabs(["Show Coordinates", "Clipped Coordinates", "Unclipped Graph", "Clipped Graph", "Compare Both"])
            with t1:
                result = p.get_vertices()
                if type(result)==str:
                    st.write(result)
                else:
                    for v in p.get_vertices():
                        st.write(v)
            with t2:
                for v in new_coords:
                        st.write(v)
            with t3:
                st.pyplot(p.draw_unclipped_window())
            with t4:
                st.pyplot(p.draw_clipped_window(new_coords))
            with t5:
                st.pyplot(p.draw_both_window(new_coords))
with line:
    st.title("Line Clipping", anchor=False)
    st.subheader("Window size", anchor=False)
    st.write("Default window size is (0, 0) and (100, 100)")
    cols = st.columns([3,3])
    with cols[0].expander("Custom window"):
        X_min = st.number_input("X_min", value=0, key=6)
        Y_min = st.number_input("Y_min", value=0, key=7)
        X_max = st.number_input("X_max", value=100, key=8)
        Y_max = st.number_input("Y_max", value=100, key=9)

    l = Line_clipping((X_min, Y_min), (X_max, Y_max))
    cols[0].subheader("Vertices", anchor=False)
    vertices = st.text_input("Coordinates", placeholder="x1,y1,x2,y2")
    if vertices!="":
        vertices = vertices.split(",")
        vertices = list(map(float, vertices))
        if len(vertices)!=4:
            st.warning("Enter complete coordinates!!!")
        else:
            st.success("Vertices are set successfully.")
            new_vertices=list()
            for i in range(0,len(vertices)-1,2):
                new_vertices.append((vertices[i], vertices[i+1]))
            l.set_line(new_vertices[0], new_vertices[1])
    if st.button("Submit", type="primary", key=10):
        curr_case = l.calc_case()
        curr_coords = l.final_coordinates(curr_case)
        with st.expander("Outputs"):
            t1,t2,t3,t4,t5 = st.tabs(["Show Coordinates", "Clipped Coordinates", "Unclipped Graph", "Clipped Graph", "Compare Both"])
            with t1:
                result = l.get_line()
                if type(result)==str:
                    st.write(result)
                else:
                    for v in l.get_line():
                        st.write(v)
            with t2:
                for v in curr_coords:
                        st.write(v)
            with t3:
                st.pyplot(l.draw_unclipped_window())
            with t4:
                st.pyplot(l.draw_clipped_window(curr_coords))
            with t5:
                st.pyplot(l.draw_both_window(curr_coords))
with point:
    st.title("Point Clipping", anchor=False)
    st.subheader("Window size", anchor=False)
    st.write("Default window size is (0, 0) and (100, 100)")
    cols = st.columns([3,3])
    with cols[0].expander("Custom window"):
        X_min = st.number_input("X_min", value=0, key=11)
        Y_min = st.number_input("Y_min", value=0, key=12)
        X_max = st.number_input("X_max", value=100, key=13)
        Y_max = st.number_input("Y_max", value=100, key=14)

    p = Point_clipping((X_min, Y_min), (X_max, Y_max))
    cols[0].subheader("Vertices", anchor=None)
    given_coords = cols[0].text_input("Coordinates", placeholder="X, Y")
    if given_coords!="":
        given_coords = given_coords.split(",")
        given_coords = list(map(float, given_coords))
        if len(given_coords)!=2:
            st.warning("Enter single X and Y coordinates!!!")
        else:
            st.success("Coordinate is set successfully.")
    if st.button("Submit", type="primary", key=15):
        curr_case = p.check(given_coords)
        with st.expander("Outputs"):
            t1,t2,t3,t4,t5 = st.tabs(["Show Coordinates", "Visibility", "Unclipped Graph", "Clipped Graph", "Compare Both"])
            with t1:
                st.write(tuple(given_coords))
            with t2:
                if curr_case==0:
                    st.warning("Not Visible.")
                else:
                    st.success("Visible.")
            with t3:
                st.pyplot(p.draw_unclipped_window())
            with t4:
                st.pyplot(p.draw_clipped_window(given_coords))
            with t5:
                st.pyplot(p.draw_both_window(given_coords))
