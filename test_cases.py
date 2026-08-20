from main import evaluate_address

TEST_CASES = [
    {"address": "42, MG Road, Bengaluru, Karnataka", "pincode": "560001", "expected": "low"},
    {"address": "House no 12, xyzxyz street, asdf", "pincode": "000000", "expected": "high"},
    {"address": "Flat 3B, Sunrise Apartments, Andheri West, Mumbai", "pincode": "400058", "expected": "low"},
    {"address": "near temple, no house number", "pincode": "110001", "expected": "medium"},
    {"address": "PO Box 999, unknown city", "pincode": "999999", "expected": "high"},
]

def run_tests():
    correct = 0
    for case in TEST_CASES:
        result = evaluate_address(case["address"], case["pincode"])
        passed = result["risk_level"] == case["expected"]
        correct += passed
        print(f"Address: {case['address'][:40]:<40} Expected: {case['expected']:<7} Got: {result['risk_level']:<7} {'✅' if passed else '❌'}")
    print(f"\nAccuracy: {correct}/{len(TEST_CASES)}")

if __name__ == "__main__":
    run_tests()
