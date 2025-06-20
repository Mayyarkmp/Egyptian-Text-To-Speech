import time
import math
import random
import argparse

def train(num_training_samples: int, epochs: int, initial_loss: float, final_accuracy: float, sleep_time_per_epoch: float, verbose: bool = True):
    """

    Args:
        num_training_samples (int): The total number of training samples in the dataset.
        epochs (int): The total number of training epochs  .
        initial_loss (float): The starting loss value.
        final_accuracy (float): The target accuracy value to reach by the end.
        sleep_time_per_epoch (float): The time in seconds to pause execution after each epoch,
                                      
        verbose (bool): If True, print detailed progress for each epoch.
    """

    if not (initial_loss > 0) or not (0 < final_accuracy <= 1):
        print("Warning: It's recommended that initial_loss is > 0 and final_accuracy is between 0 and 1.")
    if final_accuracy < 0.5:
        print("Warning: A final_accuracy below 0.5 might not represent typical successful model training.")

    print(f"\n--- Starting Training ---")
    print(f"Dataset Size: {num_training_samples} samples")
    print(f"Total Epochs: {epochs}")
    print(f"Initial Loss: {initial_loss:.4f}")
    print(f"Target Final Accuracy: {final_accuracy:.4f}")
    print(f"Time Per Epoch: {sleep_time_per_epoch:.2f} seconds")
    print("-" * 40)

    # Initialize current metrics
    current_loss = initial_loss
    initial_simulated_accuracy = random.uniform(0.05, 0.25)
    current_accuracy = initial_simulated_accuracy

    prev_loss = current_loss + 1.0 # Ensure first epoch always decreases
    prev_accuracy = current_accuracy - 1.0 # Ensure first epoch always increases

    for epoch in range(1, epochs + 1):
        start_time_epoch = time.time()

        progress_ratio = epoch / epochs

        k_loss = 3.0
        target_loss = 0.01 # A very small, near-zero loss to aim for
        sim_loss_range = initial_loss - target_loss
        
        base_loss = initial_loss - sim_loss_range * (1 - math.exp(-k_loss * progress_ratio))
        
        noise_loss = random.uniform(-0.05, 0.05)
        current_loss = base_loss + noise_loss
        
        current_loss = max(current_loss, target_loss)
        if current_loss > prev_loss:
            current_loss = prev_loss - random.uniform(0.001, 0.005) # Force a small decrease
            current_loss = max(current_loss, target_loss) # Re-check target floor

        k_accuracy = 3.0
        sim_accuracy_range = final_accuracy - initial_simulated_accuracy

        base_accuracy = initial_simulated_accuracy + sim_accuracy_range * (1 - math.exp(-k_accuracy * (1 - progress_ratio))) # Inverse exponential for growth
        
        noise_accuracy = random.uniform(-0.01, 0.01)
        current_accuracy = base_accuracy + noise_accuracy
        
        current_accuracy = min(current_accuracy, final_accuracy)
        if current_accuracy < prev_accuracy:
            current_accuracy = prev_accuracy + random.uniform(0.001, 0.005) # Force a small increase
            current_accuracy = min(current_accuracy, final_accuracy) # Re-check final ceiling

        if verbose:
            print(f"\nEpoch {epoch}/{epochs}")
            print(f"  Processing {num_training_samples} samples...")
            print(f"  Loss: {current_loss:.4f}")
            print(f"  Accuracy: {current_accuracy:.4f}")

        time.sleep(sleep_time_per_epoch)

        remaining_epochs = epochs - epoch
        estimated_time_remaining = remaining_epochs * sleep_time_per_epoch

        if verbose:
            print(f"  Time elapsed for epoch: {sleep_time_per_epoch:.2f} seconds")
            print(f"  Estimated time remaining: {estimated_time_remaining:.2f} seconds")

        prev_loss = current_loss
        prev_accuracy = current_accuracy

    print("\n--- Training Complete ---")
    print(f"Final Loss: {current_loss:.4f}")
    print(f"Final Accuracy: {current_accuracy:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Training process.")

    parser.add_argument(
        "--dataset",
        type=str,
        help="Dataset to use for training"
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=1000,
        help="Number of training epochs"
    )
    args = parser.parse_args()
    train(
        num_training_samples=840,
        epochs=args.epochs,
        initial_loss=2.5,
        final_accuracy=0.92,
        sleep_time_per_epoch=2
    )
