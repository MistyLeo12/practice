use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();
    let tx2 = tx.clone();
    std::thread::spawn(move || tx.send(5));
    std::thread::spawn(move || tx2.send(4));
    // MPSC is FIFO
    // Prints in unspecified order
    println!("{:?}", rx.recv());
    println!("{:?}", rx.recv());
}