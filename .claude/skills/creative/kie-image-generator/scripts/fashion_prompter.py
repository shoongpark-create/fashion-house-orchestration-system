
from typing import Optional

class FashionPrompter:
    """
    Fashion-specific prompt engineer for AI image generation.
    Converts simple descriptions into professional photography prompts.
    """

    STYLES = {
        "lookbook": "Professional fashion photography, editorial lookbook style, natural lighting, high fashion pose, depth of field, 8k resolution, shot on Hasselblad",
        "ghost": "Invisible ghost mannequin shot, front view, clean white background, studio lighting, high detailed fabric texture, e-commerce photography",
        "flat": "Technical flat sketch, black and white line drawing, vector style, minimal, front and back view, blueprint aesthetic",
        "detail": "Macro close-up shot, extreme detail of fabric texture, focus on stitching and material, soft lighting, 4k texture"
    }

    CONTEXTS = {
        "street": "Urban street background, concrete texture, graffiti wall, natural daylight, candid shot",
        "studio": "Clean studio background, softbox lighting, minimal props, commercial photography",
        "nature": "Outdoor nature background, golden hour sunlight, organic atmosphere, dreamy vibe"
    }

    @staticmethod
    def enhance(
        description: str,
        mode: str = "lookbook",
        context: str = "studio",
        brand_dna: str = "Kitsch Street style, vivid colors"
    ) -> str:
        """
        Builds a full prompt based on the mode and description.
        """
        base_style = FashionPrompter.STYLES.get(mode, FashionPrompter.STYLES["lookbook"])
        bg_context = FashionPrompter.CONTEXTS.get(context, FashionPrompter.CONTEXTS["studio"])
        
        # Assemble the full prompt
        prompt = (
            f"{base_style}. "
            f"Subject: {description}. "
            f"Style: {brand_dna}. "
            f"Environment: {bg_context}. "
            f"Quality: Masterpiece, award winning photography."
        )
        
        return prompt

if __name__ == "__main__":
    # Test
    print(FashionPrompter.enhance("Neon pink oversized hoodie", mode="ghost"))
