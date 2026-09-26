import streamlit as st
from main import evaluate_address

st.set_page_config(page_title="TrustCheck COD Risk Agent", page_icon="📦")

st.title("📦 TrustCheck — COD Order Risk Agent")
st.write("Enter a delivery address to get an AI-generated fraud-risk assessment.")

address = st.text_area("Delivery Address", placeholder="House no 12, xyz street, ...")
pincode = st.text_input("Pincode", placeholder="e.g. 110001")

if st.button("Evaluate Risk"):
    if not address.strip():
        st.warning("Please enter an address.")
    else:
        with st.spinner("Evaluating..."):
            try:
                result = evaluate_address(address, pincode)
                level = result.get("risk_level", "unknown")
                score = result.get("risk_score", "N/A")

                color = {"low": "green", "medium": "orange", "high": "red"}.get(level, "gray")
                st.markdown(f"### Risk Level: :{color}[{level.upper()}]")
                st.metric("Risk Score", f"{score}/100")
                st.write(f"**Reason:** {result.get('reason_code', 'N/A')}")

                flags = result.get("flags", [])
                if flags:
                    st.write("**Flags:**")
                    for f in flags:
                        st.write(f"- {f}")
            except Exception as e:
                st.error(f"Error: {e}")
