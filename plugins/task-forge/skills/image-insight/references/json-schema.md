# JSON Schema Reference

Complete JSON schema for image analysis output.

## Schema Structure

```json
{
  "metadata": {
    "confidence_score": "high/medium/low",
    "image_type": "photograph/digital art/illustration/graphic design/mixed media",
    "primary_purpose": "marketing/editorial/social media/product/portrait/landscape/abstract"
  },
  "composition": {
    "rule_applied": "rule of thirds/golden ratio/center composition/symmetry/asymmetry",
    "aspect_ratio": "width:height ratio or format description",
    "layout": "grid/single subject/multi-element/layered",
    "focal_points": ["Primary focal point", "Secondary if present"],
    "visual_hierarchy": "Eye movement path description",
    "balance": "symmetric/asymmetric/radial - with description"
  },
  "color_profile": {
    "dominant_colors": [
      {
        "color": "Specific color name",
        "hex": "#000000",
        "percentage": "approximate percentage",
        "role": "background/accent/primary subject"
      }
    ],
    "color_palette": "complementary/analogous/triadic/monochromatic/split-complementary",
    "temperature": "warm/cool/neutral",
    "saturation": "highly saturated/moderate/desaturated/black and white",
    "contrast": "high contrast/medium contrast/low contrast/soft"
  },
  "lighting": {
    "type": "natural window/artificial/mixed/studio/practical lights",
    "source_count": "single source/multiple sources - number and placement",
    "direction": "front/45-degree side/90-degree side/back/top/bottom/diffused from above",
    "directionality": "highly directional/moderately directional/diffused/omni-directional",
    "quality": "hard light/soft light/dramatic/even/gradient/sculpted",
    "intensity": "bright/moderate/low/moody/high-key/low-key",
    "contrast_ratio": "high contrast (dramatic shadows)/medium contrast/low contrast (flat)",
    "mood": "cheerful/dramatic/mysterious/calm/energetic/professional/casual",
    "shadows": {
      "type": "harsh defined edges/soft gradual edges/minimal/dramatic/absent",
      "density": "deep black/gray/transparent/faint",
      "placement": "under subject/on wall/from objects/cast patterns",
      "length": "short/medium/long"
    },
    "highlights": {
      "treatment": "blown out/preserved/subtle/dramatic/specular",
      "placement": "on face/hair/clothing/background"
    },
    "ambient_fill": "present/absent",
    "light_temperature": "warm (golden)/neutral/cool (blue)"
  },
  "technical_specs": {
    "medium": "digital photography/3D render/digital painting/vector/photo manipulation/mixed",
    "style": "realistic/hyperrealistic/stylized/minimalist/maximalist/abstract/surreal",
    "texture": "smooth/grainy/sharp/soft/painterly/glossy/matte",
    "sharpness": "tack sharp/slightly soft/deliberately soft/bokeh effect",
    "grain": "none/film grain/digital noise/intentional grain",
    "depth_of_field": "shallow/medium/deep - with subject isolation description",
    "perspective": "straight on/low angle/high angle/dutch angle/isometric/one-point/two-point"
  },
  "artistic_elements": {
    "genre": "portrait/landscape/abstract/conceptual/commercial/editorial/street/fine art",
    "influences": ["Identified artistic movement or style influence"],
    "mood": "energetic/calm/dramatic/playful/sophisticated/raw/polished",
    "atmosphere": "Overall feeling and emotional impact description",
    "visual_style": "clean/cluttered/minimal/busy/organic/geometric/fluid/structured"
  },
  "typography": {
    "present": true/false,
    "fonts": [
      {
        "type": "sans-serif/serif/script/display/handwritten",
        "weight": "thin/light/regular/medium/bold/black",
        "characteristics": "modern/vintage/playful/serious/technical"
      }
    ],
    "placement": "overlay/integrated/border/corner",
    "integration": "subtle/prominent/dominant/background"
  },
  "subject_analysis": {
    "primary_subject": "Main subject description",
    "positioning": "center/left/right/top/bottom/rule of thirds placement",
    "scale": "close-up/medium/full/environmental/macro",
    "interaction": "isolated/interacting with environment/multiple subjects",
    "facial_expression": {
      "mouth": "closed smile/open smile/slight smile/neutral/serious/pursed",
      "smile_intensity": "no smile/subtle/moderate/broad/wide",
      "eyes": "direct gaze/looking away/squinting/wide/relaxed/intense",
      "eyebrows": "raised/neutral/furrowed/relaxed",
      "overall_emotion": "happy/content/serious/playful/confident/approachable/guarded/warm/cold",
      "authenticity": "genuine/posed/candid/formal/natural"
    },
    "hair": {
      "length": "pixie/short/chin-length/shoulder-length/mid-back/long/very long",
      "cut": "blunt/layered/shaggy/undercut/fade/tapered/disconnected",
      "texture": "straight/wavy/curly/coily/kinky",
      "texture_quality": "smooth/coarse/fine/thick/thin",
      "natural_imperfections": "flyaways/frizz/uneven sections/growth patterns/cowlicks",
      "styling": "sleek/tousled/wet look/blow-dried/natural/product-heavy/messy/textured",
      "styling_detail": "Degree of styling description",
      "part": "center/side/deep side/no part/zigzag",
      "volume": "flat/moderate volume/voluminous",
      "details": "Specific features: bangs, layers, fades, etc."
    },
    "hands_and_gestures": {
      "left_hand": "Exact position and gesture",
      "right_hand": "Exact position and gesture",
      "finger_positions": "Specific details",
      "finger_interlacing": "For clasped hands: interlacing style",
      "hand_tension": "relaxed/tense/natural/posed/rigid",
      "interaction": "What hands are doing",
      "naturalness": "organic casual/deliberately posed/caught mid-motion/static formal"
    },
    "body_positioning": {
      "posture": "standing/sitting/leaning/lying",
      "angle": "facing camera/45 degree turn/profile/back to camera",
      "weight_distribution": "leaning left/right/centered/shifted",
      "shoulders": "level/tilted/rotated/hunched/back"
    }
  },
  "background": {
    "setting_type": "indoor/outdoor/studio/natural environment",
    "spatial_depth": "shallow/medium/deep",
    "elements_detailed": [
      {
        "item": "Specific object name",
        "position": "left/right/center/top/bottom with quadrant",
        "distance": "foreground/midground/background",
        "size": "dominant/medium/small",
        "condition": "new/worn/vintage/pristine/wilted/thriving",
        "specific_features": "Additional details"
      }
    ],
    "wall_surface": {
      "material": "painted drywall/concrete/brick/wood paneling/tile/wallpaper/plaster",
      "surface_treatment": "smooth paint/textured paint/raw concrete/polished concrete/exposed brick",
      "texture": "perfectly smooth/slightly textured/rough/patterned/brushed",
      "finish": "matte/satin/glossy/flat",
      "color": "Specific color with undertones",
      "color_variation": "uniform/gradient/patchy/streaked",
      "features": "Observable surface details",
      "wear_indicators": "pristine/aged/weathered/industrial/residential"
    },
    "floor_surface": {
      "material": "wood/tile/carpet/concrete/grass",
      "color": "Specific color",
      "pattern": "solid/checkered/striped/herringbone"
    },
    "objects_catalog": "List every visible object with position",
    "background_treatment": "blurred/sharp/minimal/detailed/gradient/textured"
  },
  "generation_parameters": {
    "prompts": ["Detailed technical prompt for recreating this style", "Alternative variation prompt"],
    "keywords": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
    "technical_settings": "Recommended camera/render settings",
    "post_processing": "Color grading, filters, or editing techniques"
  }
}
```

## Required Sections

All analysis output must include these 9 sections:

1. `metadata`
2. `composition`
3. `color_profile`
4. `lighting`
5. `technical_specs`
6. `artistic_elements`
7. `subject_analysis`
8. `background`
9. `generation_parameters`

The `typography` section is optional (include only if text is present in image).
