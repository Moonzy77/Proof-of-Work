import os
import time


BLOCK_SIZE = 64
ZERO_512 = bytes(BLOCK_SIZE)
BLOCK_BITS = (512).to_bytes(BLOCK_SIZE, "big")
IV_256 = bytes([1] * BLOCK_SIZE)

STUDENT_NAME = ""
TRANSACTION_COUNT = 5
TRANSACTION_SIZE = 200
NAME_TRANSACTION_INDEX = 2
POW_ZERO_BITS = 5

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "crypto5_result")


PI = [
    0xFC, 0xEE, 0xDD, 0x11, 0xCF, 0x6E, 0x31, 0x16, 0xFB, 0xC4, 0xFA, 0xDA, 0x23, 0xC5, 0x04, 0x4D,
    0xE9, 0x77, 0xF0, 0xDB, 0x93, 0x2E, 0x99, 0xBA, 0x17, 0x36, 0xF1, 0xBB, 0x14, 0xCD, 0x5F, 0xC1,
    0xF9, 0x18, 0x65, 0x5A, 0xE2, 0x5C, 0xEF, 0x21, 0x81, 0x1C, 0x3C, 0x42, 0x8B, 0x01, 0x8E, 0x4F,
    0x05, 0x84, 0x02, 0xAE, 0xE3, 0x6A, 0x8F, 0xA0, 0x06, 0x0B, 0xED, 0x98, 0x7F, 0xD4, 0xD3, 0x1F,
    0xEB, 0x34, 0x2C, 0x51, 0xEA, 0xC8, 0x48, 0xAB, 0xF2, 0x2A, 0x68, 0xA2, 0xFD, 0x3A, 0xCE, 0xCC,
    0xB5, 0x70, 0x0E, 0x56, 0x08, 0x0C, 0x76, 0x12, 0xBF, 0x72, 0x13, 0x47, 0x9C, 0xB7, 0x5D, 0x87,
    0x15, 0xA1, 0x96, 0x29, 0x10, 0x7B, 0x9A, 0xC7, 0xF3, 0x91, 0x78, 0x6F, 0x9D, 0x9E, 0xB2, 0xB1,
    0x32, 0x75, 0x19, 0x3D, 0xFF, 0x35, 0x8A, 0x7E, 0x6D, 0x54, 0xC6, 0x80, 0xC3, 0xBD, 0x0D, 0x57,
    0xDF, 0xF5, 0x24, 0xA9, 0x3E, 0xA8, 0x43, 0xC9, 0xD7, 0x79, 0xD6, 0xF6, 0x7C, 0x22, 0xB9, 0x03,
    0xE0, 0x0F, 0xEC, 0xDE, 0x7A, 0x94, 0xB0, 0xBC, 0xDC, 0xE8, 0x28, 0x50, 0x4E, 0x33, 0x0A, 0x4A,
    0xA7, 0x97, 0x60, 0x73, 0x1E, 0x00, 0x62, 0x44, 0x1A, 0xB8, 0x38, 0x82, 0x64, 0x9F, 0x26, 0x41,
    0xAD, 0x45, 0x46, 0x92, 0x27, 0x5E, 0x55, 0x2F, 0x8C, 0xA3, 0xA5, 0x7D, 0x69, 0xD5, 0x95, 0x3B,
    0x07, 0x58, 0xB3, 0x40, 0x86, 0xAC, 0x1D, 0xF7, 0x30, 0x37, 0x6B, 0xE4, 0x88, 0xD9, 0xE7, 0x89,
    0xE1, 0x1B, 0x83, 0x49, 0x4C, 0x3F, 0xF8, 0xFE, 0x8D, 0x53, 0xAA, 0x90, 0xCA, 0xD8, 0x85, 0x61,
    0x20, 0x71, 0x67, 0xA4, 0x2D, 0x2B, 0x09, 0x5B, 0xCB, 0x9B, 0x25, 0xD0, 0xBE, 0xE5, 0x6C, 0x52,
    0x59, 0xA6, 0x74, 0xD2, 0xE6, 0xF4, 0xB4, 0xC0, 0xD1, 0x66, 0xAF, 0xC2, 0x39, 0x4B, 0x63, 0xB6,
]

TAU = [
    0, 8, 16, 24, 32, 40, 48, 56,
    1, 9, 17, 25, 33, 41, 49, 57,
    2, 10, 18, 26, 34, 42, 50, 58,
    3, 11, 19, 27, 35, 43, 51, 59,
    4, 12, 20, 28, 36, 44, 52, 60,
    5, 13, 21, 29, 37, 45, 53, 61,
    6, 14, 22, 30, 38, 46, 54, 62,
    7, 15, 23, 31, 39, 47, 55, 63,
]

A_MATRIX = [
    0x8E20FAA72BA0B470, 0x47107DDD9B505A38, 0xAD08B0E0C3282D1C, 0xD8045870EF14980E,
    0x6C022C38F90A4C07, 0x3601161CF205268D, 0x1B8E0B0E798C13C8, 0x83478B07B2468764,
    0xA011D380818E8F40, 0x5086E740CE47C920, 0x2843FD2067ADEA10, 0x14AFF010BDD87508,
    0x0AD97808D06CB404, 0x05E23C0468365A02, 0x8C711E02341B2D01, 0x46B60F011A83988E,
    0x90DAB52A387AE76F, 0x486DD4151C3DFDB9, 0x24B86A840E90F0D2, 0x125C354207487869,
    0x092E94218D243CBA, 0x8A174A9EC8121E5D, 0x4585254F64090FA0, 0xACCC9CA9328A8950,
    0x9D4DF05D5F661451, 0xC0A878A0A1330AA6, 0x60543C50DE970553, 0x302A1E286FC58CA7,
    0x18150F14B9EC46DD, 0x0C84890AD27623E0, 0x0642CA05693B9F70, 0x0321658CBA93C138,
    0x86275DF09CE8AAA8, 0x439DA0784E745554, 0xAFC0503C273AA42A, 0xD960281E9D1D5215,
    0xE230140FC0802984, 0x71180A8960409A42, 0xB60C05CA30204D21, 0x5B068C651810A89E,
    0x456C34887A3805B9, 0xAC361A443D1C8CD2, 0x561B0D22900E4669, 0x2B838811480723BA,
    0x9BCF4486248D9F5D, 0xC3E9224312C8C1A0, 0xEFFA11AF0964EE50, 0xF97D86D98A327728,
    0xE4FA2054A80B329C, 0x727D102A548B194E, 0x39B008152ACB8227, 0x9258048415EB419D,
    0x492C024284FBAEC0, 0xAA16012142F35760, 0x550B8E9E21F7A530, 0xA48B474F9EF5DC18,
    0x70A6A56E2440598E, 0x3853DC371220A247, 0x1CA76E95091051AD, 0x0EDD37C48A08A6D8,
    0x07E095624504536C, 0x8D70C431AC02A736, 0xC83862965601DD1B, 0x641C314B2B8EE083,
]

C_CONSTANTS = [
    bytes.fromhex("b1085bda1ecadae9ebcb2f81c0657c1f2f6a76432e45d016714eb88d7585c4fc4b7ce09192676901a2422a08a460d31505767436cc744d23dd806559f2a64507"),
    bytes.fromhex("6fa3b58aa99d2f1a4fe39d460f70b5d7f3feea720a232b9861d55e0f16b501319ab5176b12d699585cb561c2db0aa7ca55dda21bd7cbcd56e679047021b19bb7"),
    bytes.fromhex("f574dcac2bce2fc70a39fc286a3d843506f15e5f529c1f8bf2ea7514b1297b7bd3e20fe490359eb1c1c93a376062db09c2b6f443867adb31991e96f50aba0ab2"),
    bytes.fromhex("ef1fdfb3e81566d2f948e1a05d71e4dd488e857e335c3c7d9d721cad685e353fa9d72c82ed03d675d8b71333935203be3453eaa193e837f1220cbebc84e3d12e"),
    bytes.fromhex("4bea6bacad4747999a3f410c6ca923637f151c1f1686104a359e35d7800fffbdbfcd1747253af5a3dfff00b723271a167a56a27ea9ea63f5601758fd7c6cfe57"),
    bytes.fromhex("ae4faeae1d3ad3d96fa4c33b7a3039c02d66c4f95142a46c187f9ab49af08ec6cffaa6b71c9ab7b40af21f66c2bec6b6bf71c57236904f35fa68407a46647d6e"),
    bytes.fromhex("f4c70e16eeaac5ec51ac86febf240954399ec6c7e6bf87c9d3473e33197a93c90992abc52d822c3706476983284a05043517454ca23c4af38886564d3a14d493"),
    bytes.fromhex("9b1f5b424d93c9a703e7aa020c6e41414eb7f8719c36de1e89b4443b4ddbc49af4892bcb929b069069d18d2bd1a5c42f36acc2355951a8d9a47f0dd4bf02e71e"),
    bytes.fromhex("378f5a541631229b944c9ad8ec165fde3a7d3a1b258942243cd955b7e00d0984800a440bdbb2ceb17b2b8a9aa6079c540e38dc92cb1f2a607261445183235adb"),
    bytes.fromhex("abbedea680056f52382ae548b2e4f3f38941e71cff8a78db1fffe18a1b3361039fe76702af69334b7a1e6c303b7652f43698fad1153bb6c374b4c7fb98459ced"),
    bytes.fromhex("7bcd9ed0efc889fb3002c6cd635afe94d8fa6bbbebab076120018021148466798a1d71efea48b9caefbacd1d7d476e98dea2594ac06fd85d6bcaa4cd81f32d1b"),
    bytes.fromhex("378ee767f11631bad21380b00449b17acda43c32bcdf1d77f82012d430219f9b5d80ef9d1891cc86e71da4aa88e12852faf417d5d9b21b9948bc924af11bd720"),
]


P = int("EE8172AE8996608FB69359B89EB82A69854510E2977A4D63BC97322CE5DC3386EA0A12B343E9190F23177539845839786BB0C345D165976EF2195EC9B1C379E3", 16)
Q = int("98915E7EC8265EDFCDA31E88F24809DDB064BDC7285DD50D7289F0AC6F49DD2D", 16)
G = int("9E96031500C8774A869582D4AFDE2127AFAD2538B4B6270A6F7C8837B50D50F206755984A49E509304D648BE2AB5AAB18EBE2CD46AC3D8495B142AA6CE23E21C", 16)


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def add_mod_512(a, b):
    total = (int.from_bytes(a, "big") + int.from_bytes(b, "big")) % (1 << 512)
    return total.to_bytes(BLOCK_SIZE, "big")


def s_transform(data):
    return bytes(PI[byte] for byte in data)


def p_transform(data):
    return bytes(data[index] for index in TAU)


def l_transform(data):
    result = bytearray()
    offset = 0
    while offset < BLOCK_SIZE:
        block = data[offset:offset + 8]
        value = 0
        byte_index = 0
        while byte_index < 8:
            byte = block[byte_index]
            bit_index = 0
            while bit_index < 8:
                if byte & (1 << (7 - bit_index)):
                    value ^= A_MATRIX[byte_index * 8 + bit_index]
                bit_index += 1
            byte_index += 1
        result.extend(value.to_bytes(8, "big"))
        offset += 8
    return bytes(result)


def lps_transform(data):
    return l_transform(p_transform(s_transform(data)))


def e_transform(key, message):
    state = message
    round_key = key
    index = 0
    while index < len(C_CONSTANTS):
        state = lps_transform(xor_bytes(state, round_key))
        round_key = lps_transform(xor_bytes(round_key, C_CONSTANTS[index]))
        index += 1
    return xor_bytes(state, round_key)


def g_transform(n, h, message):
    key = lps_transform(xor_bytes(h, n))
    encrypted = e_transform(key, message)
    return xor_bytes(xor_bytes(encrypted, h), message)


def pad_message_block(block):
    return b"\x00" * (BLOCK_SIZE - len(block) - 1) + b"\x01" + block


def streebog_256(data):
    h = IV_256
    n = ZERO_512
    sigma = ZERO_512
    tail = data

    while len(tail) >= BLOCK_SIZE:
        block = tail[-BLOCK_SIZE:]
        tail = tail[:-BLOCK_SIZE]
        h = g_transform(n, h, block)
        n = add_mod_512(n, BLOCK_BITS)
        sigma = add_mod_512(sigma, block)

    block = pad_message_block(tail)
    h = g_transform(n, h, block)
    n = add_mod_512(n, (len(tail) * 8).to_bytes(BLOCK_SIZE, "big"))
    sigma = add_mod_512(sigma, block)
    h = g_transform(ZERO_512, h, n)
    h = g_transform(ZERO_512, h, sigma)
    return h[:32]


def hash_file(filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    return streebog_256(data)


class HashGenerator:
    def __init__(self, student_name):
        seed = student_name.encode("utf-8")
        if len(seed) > BLOCK_SIZE:
            seed = seed[:BLOCK_SIZE]
        self.seed_block = seed.ljust(BLOCK_SIZE, b"\x00")
        self.h0 = streebog_256(self.seed_block)
        self.index = 1
        self.buffer = b""

    def next_block(self):
        block = streebog_256(self.h0 + self.index.to_bytes(32, "big"))
        self.index += 1
        return block

    def next_bytes(self, count):
        while len(self.buffer) < count:
            self.buffer += self.next_block()
        result = self.buffer[:count]
        self.buffer = self.buffer[count:]
        return result

    def next_number(self, modulus):
        value = int.from_bytes(self.next_bytes(32), "big")
        return (value % (modulus - 1)) + 1


class LabState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.student_name = STUDENT_NAME
        self.generator = HashGenerator(STUDENT_NAME)
        self.private_key = None
        self.public_key = None
        self.transactions = []
        self.signatures = []
        self.signed_hashes = []
        self.merkle = None
        self.block_size = None
        self.previous_hash = None
        self.timestamp_bytes = None
        self.timestamp_text = None
        self.nonce = None
        self.block_hash = None


STATE = None


def print_header():
    print("\n" + "=" * 72)
    print("                             Proof of Work")
    print("=" * 72)


def print_section(title):
    print("\n" + "-" * 72)
    print(f"   {title}")
    print("-" * 72)


def enter():
    input("\nНажмите Enter для продолжения...")


def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def write_text_file(filename, text):
    file = open(filename, "w", encoding="utf-8")
    file.write(text)
    file.close()


def write_binary_file(filename, data):
    file = open(filename, "wb")
    file.write(data)
    file.close()


def input_path(prompt):
    while True:
        path = input(prompt + ": ").strip()
        if path:
            return path
        print("Путь не может быть пустым.")


def print_parameters():
    print_section("ПАРАМЕТРЫ")
    print("Студент:", STATE.student_name)
    print("p =", hex(P)[2:])
    print("q =", hex(Q)[2:])
    print("g =", hex(G)[2:])
    print("Размер транзакции =", TRANSACTION_SIZE, "байт")
    print("Количество транзакций =", TRANSACTION_COUNT)
    print("Требование PoW =", POW_ZERO_BITS, "нулевых бит")
    print("Папка результатов =", OUTPUT_DIR)
    enter()


def schnorr_challenge(r_value, public_key, message):
    p_size = (P.bit_length() + 7) // 8
    data = r_value.to_bytes(p_size, "big") + public_key.to_bytes(p_size, "big") + message
    e_value = int.from_bytes(streebog_256(data), "big") % Q
    if e_value == 0:
        e_value = 1
    return e_value


def ensure_keys():
    if STATE.private_key is None or STATE.public_key is None:
        STATE.private_key = STATE.generator.next_number(Q)
        STATE.public_key = pow(G, STATE.private_key, P)


def sign_message(message):
    ensure_keys()
    while True:
        k_value = STATE.generator.next_number(Q)
        r_value = pow(G, k_value, P)
        e_value = schnorr_challenge(r_value, STATE.public_key, message)
        s_value = (k_value + e_value * STATE.private_key) % Q
        if s_value != 0:
            return r_value, s_value, e_value, k_value


def verify_signature(message, public_key, r_value, s_value):
    if not (1 < r_value < P):
        return False
    if not (0 < s_value < Q):
        return False
    if pow(r_value, Q, P) != 1:
        return False
    e_value = schnorr_challenge(r_value, public_key, message)
    left = pow(G, s_value, P)
    right = (r_value * pow(public_key, e_value, P)) % P
    return left == right


def build_transaction(index):
    data = bytearray(STATE.generator.next_bytes(TRANSACTION_SIZE))
    if index == NAME_TRANSACTION_INDEX:
        name_bytes = STATE.student_name.encode("utf-8")
        if len(name_bytes) > TRANSACTION_SIZE:
            name_bytes = name_bytes[:TRANSACTION_SIZE]
        data[:len(name_bytes)] = name_bytes
    return bytes(data)


def build_signed_blob(transaction, signature):
    r_value = signature[0]
    s_value = signature[1]
    p_size = (P.bit_length() + 7) // 8
    q_size = (Q.bit_length() + 7) // 8
    return transaction + r_value.to_bytes(p_size, "big") + s_value.to_bytes(q_size, "big")


def ensure_transactions():
    if STATE.transactions:
        return

    ensure_keys()
    index = 0
    while index < TRANSACTION_COUNT:
        transaction = build_transaction(index)
        signature = sign_message(transaction)
        signed_blob = build_signed_blob(transaction, signature)
        STATE.transactions.append(transaction)
        STATE.signatures.append(signature)
        STATE.signed_hashes.append(streebog_256(signed_blob))
        index += 1


def merkle_root(hashes):
    current = hashes[:]
    while len(current) > 1:
        if len(current) % 2 == 1:
            current.append(current[-1])
        next_level = []
        index = 0
        while index < len(current):
            next_level.append(streebog_256(current[index] + current[index + 1]))
            index += 2
        current = next_level
    return current[0]


def ensure_merkle():
    if STATE.merkle is None:
        ensure_transactions()
        STATE.merkle = merkle_root(STATE.signed_hashes)


def make_timestamp_bytes():
    now = time.localtime()
    year = now.tm_year % 100
    timestamp = bytes([now.tm_hour, now.tm_mday, now.tm_mon, year])
    text = f"{now.tm_hour:02d}:{now.tm_mday:02d}:{now.tm_mon:02d}:{now.tm_year}"
    return timestamp, text


def has_zero_bits(digest, bits):
    full_bytes = bits // 8
    remaining_bits = bits % 8

    index = 0
    while index < full_bytes:
        if digest[index] != 0:
            return False
        index += 1

    if remaining_bits == 0:
        return True

    mask = 0xFF << (8 - remaining_bits)
    return (digest[full_bytes] & mask) == 0


def ensure_block():
    if STATE.block_hash is not None:
        return

    ensure_merkle()
    block_size = bytearray(STATE.generator.next_bytes(4))
    index = 0
    while index < 4:
        if block_size[index] == 0:
            block_size[index] = 1
        index += 1

    STATE.block_size = bytes(block_size)
    STATE.previous_hash = STATE.generator.next_bytes(32)
    STATE.timestamp_bytes, STATE.timestamp_text = make_timestamp_bytes()

    header_without_nonce = STATE.block_size + STATE.previous_hash + STATE.merkle + STATE.timestamp_bytes
    nonce = 0
    while nonce <= 0xFFFFFFFF:
        digest = streebog_256(header_without_nonce + nonce.to_bytes(4, "big"))
        if has_zero_bits(digest, POW_ZERO_BITS):
            STATE.nonce = nonce
            STATE.block_hash = digest
            return
        nonce += 1


def save_results():
    ensure_output_dir()
    ensure_block()

    write_text_file(os.path.join(OUTPUT_DIR, "private_key.txt"), "x=" + hex(STATE.private_key)[2:] + "\n")
    write_text_file(os.path.join(OUTPUT_DIR, "public_key.txt"), "y=" + hex(STATE.public_key)[2:] + "\n")

    result_lines = []
    result_lines.append("СТУДЕНТ: " + STATE.student_name)
    result_lines.append("h0=" + STATE.generator.h0.hex())
    result_lines.append("p=" + hex(P)[2:])
    result_lines.append("q=" + hex(Q)[2:])
    result_lines.append("g=" + hex(G)[2:])
    result_lines.append("x=" + hex(STATE.private_key)[2:])
    result_lines.append("y=" + hex(STATE.public_key)[2:])
    result_lines.append("")

    index = 0
    while index < TRANSACTION_COUNT:
        tx_name = "tx_" + str(index + 1) + ".bin"
        sig_name = "sig_" + str(index + 1) + ".txt"
        transaction = STATE.transactions[index]
        signature = STATE.signatures[index]
        verified = verify_signature(transaction, STATE.public_key, signature[0], signature[1])

        write_binary_file(os.path.join(OUTPUT_DIR, tx_name), transaction)
        write_text_file(
            os.path.join(OUTPUT_DIR, sig_name),
            "R=" + hex(signature[0])[2:] + "\n" +
            "s=" + hex(signature[1])[2:] + "\n" +
            "e=" + hex(signature[2])[2:] + "\n" +
            "ok=" + str(verified) + "\n",
        )

        result_lines.append(tx_name)
        result_lines.append("hash_tx=" + streebog_256(transaction).hex())
        result_lines.append("R=" + hex(signature[0])[2:])
        result_lines.append("s=" + hex(signature[1])[2:])
        result_lines.append("e=" + hex(signature[2])[2:])
        result_lines.append("ok=" + str(verified))
        result_lines.append("signed_hash=" + STATE.signed_hashes[index].hex())
        result_lines.append("")
        index += 1

    result_lines.append("merkle_root=" + STATE.merkle.hex())
    result_lines.append("block_size=" + STATE.block_size.hex())
    result_lines.append("previous_hash=" + STATE.previous_hash.hex())
    result_lines.append("timestamp=" + STATE.timestamp_text)
    result_lines.append("timestamp_bytes=" + STATE.timestamp_bytes.hex())
    result_lines.append("nonce=" + str(STATE.nonce))
    result_lines.append("block_hash=" + STATE.block_hash.hex())

    write_text_file(os.path.join(OUTPUT_DIR, "result.txt"), "\n".join(result_lines) + "\n")



def hash_menu():
    while True:
        print_section("ХЭШ-ФУНКЦИЯ СТРИБОГ-256")
        print("1. Показать h0 для фамилии и имени")
        print("2. Посчитать хэш строки")
        print("3. Посчитать хэш файла")
        print("4. Назад")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            print("\nseed =", STATE.generator.seed_block.hex())
            print("h0   =", STATE.generator.h0.hex())
            enter()
        elif choice == "2":
            text = input("Введите строку: ")
            print("hash =", streebog_256(text.encode("utf-8")).hex())
            enter()
        elif choice == "3":
            filename = input_path("Введите путь к файлу")
            print("hash =", hash_file(filename).hex())
            enter()
        elif choice == "4":
            break
        else:
            print("Неверный пункт меню.")


def generator_menu():
    while True:
        print_section("ГЕНЕРАТОР ПСЕВДОСЛУЧАЙНЫХ ЧИСЕЛ")
        print("1. Показать h0")
        print("2. Сгенерировать 32 байта")
        print("3. Сгенерировать 64 байта")
        print("4. Назад")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            print("\nseed =", STATE.generator.seed_block.hex())
            print("h0   =", STATE.generator.h0.hex())
            print("i    =", STATE.generator.index)
            enter()
        elif choice == "2":
            print("\nbytes32 =", STATE.generator.next_bytes(32).hex())
            print("i       =", STATE.generator.index)
            enter()
        elif choice == "3":
            print("\nbytes64 =", STATE.generator.next_bytes(64).hex())
            print("i       =", STATE.generator.index)
            enter()
        elif choice == "4":
            break
        else:
            print("Неверный пункт меню.")


def schnorr_menu():
    while True:
        print_section("ПОДПИСЬ ШНОРРА")
        print("1. Показать параметры p, q, g")
        print("2. Сгенерировать и показать ключевую пару")
        print("3. Подписать строку")
        print("4. Назад")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            print("\np =", hex(P)[2:])
            print("q =", hex(Q)[2:])
            print("g =", hex(G)[2:])
            enter()
        elif choice == "2":
            ensure_keys()
            print("\nx =", hex(STATE.private_key)[2:])
            print("y =", hex(STATE.public_key)[2:])
            enter()
        elif choice == "3":
            message = input("Введите строку: ").encode("utf-8")
            signature = sign_message(message)
            verified = verify_signature(message, STATE.public_key, signature[0], signature[1])
            print("\nR =", hex(signature[0])[2:])
            print("s =", hex(signature[1])[2:])
            print("e =", hex(signature[2])[2:])
            print("ok =", verified)
            enter()
        elif choice == "4":
            break
        else:
            print("Неверный пункт меню.")


def transaction_menu():
    while True:
        print_section("ТРАНЗАКЦИИ И ДЕРЕВО МЕРКЛА")
        print("1. Сгенерировать 5 транзакций и подписи")
        print("2. Показать краткую информацию по транзакциям")
        print("3. Показать корень дерева Меркла")
        print("4. Назад")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            ensure_transactions()
            print("\nТранзакции и подписи сформированы.")
            print("В транзакцию №3 записано имя студента.")
            enter()
        elif choice == "2":
            ensure_transactions()
            index = 0
            while index < TRANSACTION_COUNT:
                signature = STATE.signatures[index]
                verified = verify_signature(STATE.transactions[index], STATE.public_key, signature[0], signature[1])
                print("\ntx_" + str(index + 1))
                print("hash_tx     =", streebog_256(STATE.transactions[index]).hex())
                print("R           =", hex(signature[0])[2:])
                print("s           =", hex(signature[1])[2:])
                print("ok          =", verified)
                print("signed_hash =", STATE.signed_hashes[index].hex())
                index += 1
            enter()
        elif choice == "3":
            ensure_merkle()
            print("\nmerkle_root =", STATE.merkle.hex())
            enter()
        elif choice == "4":
            break
        else:
            print("Неверный пункт меню.")


def block_menu():
    while True:
        print_section("ЗАГОЛОВОК БЛОКА И PROOF OF WORK")
        print("1. Сформировать блок и подобрать nonce")
        print("2. Показать данные блока")
        print("3. Назад")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            ensure_block()
            print("\nnonce      =", STATE.nonce)
            print("block_hash =", STATE.block_hash.hex())
            enter()
        elif choice == "2":
            ensure_block()
            print("\nblock_size      =", STATE.block_size.hex())
            print("previous_hash   =", STATE.previous_hash.hex())
            print("merkle_root     =", STATE.merkle.hex())
            print("timestamp       =", STATE.timestamp_text)
            print("timestamp_bytes =", STATE.timestamp_bytes.hex())
            print("nonce           =", STATE.nonce)
            print("block_hash      =", STATE.block_hash.hex())
            enter()
        elif choice == "3":
            break
        else:
            print("Неверный пункт меню.")


def run_full_assignment():
    reset_session()
    ensure_block()
    save_results()
    print_section("РЕЗУЛЬТАТ")
    print("Все файлы сохранены в папке:")
    print(OUTPUT_DIR)
    print("merkle_root =", STATE.merkle.hex())
    print("nonce       =", STATE.nonce)
    print("block_hash  =", STATE.block_hash.hex())
    enter()


def menu():
    while True:
        print("\nВыберите действие:")
        print("1. Параметры задания")
        print("2. Хэш-функция Стрибог-256")
        print("3. Генератор псевдослучайных чисел")
        print("4. Подпись Шнорра")
        print("5. Транзакции и дерево Меркла")
        print("6. Заголовок блока и Proof of Work")
        print("7. Выполнить всю практическую работу")
        print("8. Сбросить текущую сессию")
        print("9. Выход")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            print_parameters()
        elif choice == "2":
            hash_menu()
        elif choice == "3":
            generator_menu()
        elif choice == "4":
            schnorr_menu()
        elif choice == "5":
            transaction_menu()
        elif choice == "6":
            block_menu()
        elif choice == "7":
            run_full_assignment()
        elif choice == "8":
            reset_session()
            print("\nТекущая сессия сброшена.")
            enter()
        elif choice == "9":
            print("Завершение программы.")
            break
        else:
            print("Неверный пункт меню.")


def main():
    global STUDENT_NAME, STATE
    print_header()
    
    STUDENT_NAME = input("\nВведите ваше ФИО (фамилия и имя): ").strip()
    while not STUDENT_NAME:
        STUDENT_NAME = input("ФИО не может быть пустым. Повторите ввод: ").strip()
    
    STATE = LabState()
    menu()


if __name__ == "__main__":
    main()
